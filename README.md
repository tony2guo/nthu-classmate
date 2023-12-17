# NTHU Classmate

## Overview

This tool allows you to retrieve and analyze information about National Tsing Hua University (NTHU) classmates from the [Academic Information System](https://www.ccxp.nthu.edu.tw/ccxp/INQUIRE/). It has been tested in Python 3.12 and Google Chrome Version 120.0.6099.71 (Official Build) (64-bit). Due to personal data protection regulations, classmate data in the Academic Information System will be unavailable after February 1, 2024.

An alternative method for retrieving classmate data can be found [here](https://replit.com/@ares57/Student-Lists-Downloader).

## Installation

1. Create a virtual environment:

   ```bash
   conda create -n classmate python=3.12
   ```

2. Activate the virtual environment:

   ```bash
   conda activate classmate
   ```

3. Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Run the script to fetch classmate data:

   ```bash
   python get_classmate.py
   ```
   The Academic Information System page will pop up; please manually login, then the program will take over. Wait for it to finish, and data will be saved to ./classmate/*.csv

2. Analyze course data:

   ```bash
   jupyter nbconvert --output-dir classmate --to html --execute --no-input analyze_courses.ipynb
   ```
   analyze_courses.html will be saved to ./classmate/

3. Combining classmates and courses:

   ```bash
   jupyter execute combine_classmates_courses.ipynb
   ```
   classmates.csv will be saved to ./classmate/

4. Analyze classmates data:

   ```bash
   jupyter nbconvert --output-dir classmate --to html --execute --no-input analyze_classmates.ipynb
   ```
   analyze_classmates.html will be saved to ./classmate/

## Additional Resources

- Course code mappings to departments and colleges can be found [here](https://curricul.site.nthu.edu.tw/p/406-1208-189767,r8789.php?Lang=zh-tw) and saved as `course_code.csv`.

- Understanding the student ID encoding principles at NTHU starting from the 100th academic year can be found [here](https://registra.site.nthu.edu.tw/var/file/211/1211/img/327248576.pdf).

- The following JSON files can assist in parsing student IDs to departments and colleges:
  - `college.json`
  - `department.json`
  - `department_graduate.json`
  - `class_id.json`

Feel free to explore and customize the code for your specific needs! If you encounter any issues or have suggestions for improvement, please let me know.
