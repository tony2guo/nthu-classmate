import re
import time
from io import StringIO
from pathlib import Path

import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class GetClassmate:
    def __init__(self):
        # Initialize the Chrome driver
        self.driver = webdriver.Chrome()

    def close_driver(self):
        # Close the Chrome driver
        self.driver.quit()

    def get_classmate(self, path="classmate"):
        path = Path(path)
        path.mkdir(parents=True, exist_ok=True)

        # Login and get the classmate
        self.driver.get("https://www.ccxp.nthu.edu.tw/ccxp/INQUIRE/index.php")
        print("Please login manually")
        WebDriverWait(self.driver, 600).until(
            expected_conditions.visibility_of_element_located(
                (
                    By.XPATH,
                    "//frame",
                )
            )
        )
        print("Login success")
        # click to the course list
        self.driver.switch_to.frame(1)
        self.driver.find_element(
            By.XPATH, "//tr[contains(., 'transcript')]/td[1]/a"
        ).click()
        self.driver.find_element(
            By.XPATH, "//span[contains(., 'participants')]"
        ).click()
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame(2)
        # get the course list
        courses_html = self.driver.page_source
        courses = pd.read_html(StringIO(courses_html))[0]
        courses.iloc[:, 1:].to_csv(path / "courses.csv", index=False)
        course_count = len(courses)
        # get classmates for each course
        for index, row in courses.iterrows():
            time.sleep(1)
            course_id = row["科號"]
            course_name = row["課程名稱"]
            print(f"{index + 1}/{course_count} {course_id} {course_name}")
            self.driver.find_element(
                By.CSS_SELECTOR, f"tr:nth-child({index + 2}) #cou_key"
            ).click()
            self.driver.find_element(By.NAME, "Submit").click()

            classmate_html = self.driver.page_source
            classmate = pd.read_html(StringIO(classmate_html))[2]
            classmate.columns = classmate.iloc[0]
            df = classmate[1:]

            # make sure file name is valid for Windows
            file_name = re.sub(r'[\\/*?:"<>|]', "", f"{course_id} {course_name}")
            df.iloc[:, 2:].to_csv(path / f"{file_name}.csv", index=False)
            print(df.iloc[:, 2:])

            # return to course list
            self.driver.find_element(By.NAME, "Submit").click()


if __name__ == "__main__":
    classmate = GetClassmate()
    classmate.get_classmate()
    classmate.close_driver()
