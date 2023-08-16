
"""
Author : Abhishek Yadav
Description: Automation Testing Login
Version : 1.0
Date: 14-Aug-2023
Azure Ticket Link : https://dev.azure.com/ShorthillsCampus/Training%20Batch%202023/_workitems/edit/3058

"""
import os
from dotenv import load_dotenv
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class HackerRankAutomation:
    def __init__(self):
        self.driver = self.setup_driver()

    def setup_driver(self):
        service_obj = Service(os.getcwd() + '/drivers/chromedriver')
        driver = webdriver.Chrome(service=service_obj)
        return driver

    def login(self):
        load_dotenv()
        
        self.driver.get('https://www.hackerrank.com/auth/login')
        self.driver.maximize_window()
        wait = WebDriverWait(self.driver, 10)

        # getting the username, password fields and getting login button
        login_username = wait.until(EC.visibility_of_element_located((By.NAME, "username")))
        login_password = wait.until(EC.visibility_of_element_located((By.NAME, "password")))
        login_btn = wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[4]/div/div/div/div[2]/div[2]/div/div/div[2]/div/div/div[2]/div[1]/form/div[4]/button")))

        # sending username, password and logging in
        login_username.send_keys(os.getenv("HACKERRANK_USERNAME"))
        login_password.send_keys(os.getenv("HACKERRANK_PASSWORD"))
        login_btn.click()

        # test for login success
        received_title = self.driver.title
        actual_title = "HackerRank"
        user_profile = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "user-avatar-placeholder")))

        if user_profile and received_title == actual_title:
            print("Login Successful!")
        else:
            print("Login Failed!")

    def navigate_to_python_page(self):
        wait = WebDriverWait(self.driver, 10)
        
        # getting python page navigation link
        python_redirect = wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[4]/div/div/div/div/div[3]/div/section[3]/div[2]/div/div/ul/li[8]/a")))
        python_redirect.click()

        # test for python page redirect success
        rank_and_points_bar = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "score-info")))
        if rank_and_points_bar:
            print("Redirected to python page sucessfully!")
        else:
            print("Redirect to python page was unsucessful!")

    def select_challenge_and_upload_code(self):
        wait = WebDriverWait(self.driver, 10)
        
        # selecting loop based challenge and opeaning it
        challenge = wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[4]/div/div/div/div/div[3]/div/div/div/section[1]/div[2]/div/a[4]/div/div[1]/div/header/div[2]/div/div/button")))
        challenge.click()
        
        # test for challenge page load success
        toolbar = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'editor-toolbar')))
        if(toolbar):
            print("Challenge opeaned successfully!")
        else:
            print("There is some problem occured in opening challenge")
        

        # using solution code upload option
        upload_code = wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[4]/div/div/div/div/div[3]/div/section/div/div/div/div[2]/div/div[3]/div/section/div[1]/div/div[2]/div/div[2]/div[1]/button')))
        upload_code.click()

        # confirmation before uploding
        upload_file_confirm = wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[6]/div/div/div/section/div/div[2]/div/button[2]')))
        upload_file_confirm.click()

        # selecting programming language of solution
        select_lang = wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[6]/div/div/div/section/div/div[2]/form/div[2]/div/select/option[28]')))
        select_lang.click()

        #Selecting file
        hidden_element = self.driver.execute_script('return document.querySelector(".d-none");')
        hidden_element.send_keys("/home/shtlp_0146/Desktop/hacker_rank_auto/submissions/loop.py")

        # 3sec delay for files explorer to open
        time.sleep(1)


        # uploading the selected file
        upload = wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[6]/div/div/div/section/div/div[2]/form/div[3]/div/button')))
        upload.click()
        time.sleep(1) # process the upload

        # refresh makes upload work correctly
        self.driver.refresh()
        
        # sumbit the code to run it with test cases 
        submit = wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[4]/div/div/div/div/div[3]/div/section/div/div/div/div[2]/div/div[3]/div/section/div[1]/div/div[2]/div/div[1]/div[2]/button[1]')))
        submit.click()
        
        # successful submission test
        congrats_msg = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'submission-message')))
        if(congrats_msg):
            print("Congratulations! \nYou solved this challenge")
        else:
            print("Test Cases Failed")

        time.sleep(10)

    def quit(self):
        self.driver.quit()


automation = HackerRankAutomation()
automation.login()
automation.navigate_to_python_page()
automation.select_challenge_and_upload_code()
automation.quit()

