#!/usr/bin/env python

"""main.py: This script will go to pollev.com and fill in a dumb questionarre with random answer so that you don't have to attend class to get credit."""

__author__      = "Evan Tobin"


from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os
from dotenv import load_dotenv

def main():
    if(not check_if_online()):
       exit()

    driver.find_element(By.CLASS_NAME, "pe-text-field__input").send_keys(STUDENT_ID)
    driver.find_element(By.CLASS_NAME, "pe-button__button").click()
    answer_questions()


def check_if_online():
    for i in range(0, 999):
        print(f"Attempting to connect to https://pollev.com/{PROFESSOR_NAME}{(i-1):03}")
        try:
            driver.find_element(By.CLASS_NAME, 'pe-text-field__input').clear()
            driver.find_element(By.CLASS_NAME, 'pe-text-field__input').send_keys(f'{PROFESSOR_NAME}{i:03}')
            driver.find_element(By.CLASS_NAME, "pollev-home-join__submit").click()
        except Exception:
            time.sleep(0.5)
            if(driver.current_url == f'https://pollev.com/{PROFESSOR_NAME}{(i-1):03}'):
                print("Sucesssful connection!")
                return True;
            driver.get("https://pollev.com")
            continue;
    return False

def answer_questions():
    # TODO iterate through each question and choose a random option
    print()


if __name__ == '__main__':
    # Load environment variables from the .env file in the current directory
    load_dotenv()
    PROFESSOR_NAME = os.getenv("PROFESSOR_NAME")
    STUDENT_ID = os.getenv("STUDENT_ID")
    
    if(not (PROFESSOR_NAME and STUDENT_ID)):
        print("ERROR, must provide the professor_name and student_id in the .env file, read the README for instructions.")
        exit()

    driver = webdriver.Chrome()
    driver.get("https://pollev.com")

    time.sleep(1)
    main()
