import time
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By

class Element_Selector:
    


    def click(self,xpath,driver):
        element =driver.find_element(By.XPATH, xpath)
        element.click()

    def clear_input(self,xpath,driver):
        element = driver.find_element(By.XPATH,xpath)
        element.clear()

    def type_slowly(self,word,xpath,driver,speed):
        input_field = driver.find_element(By.XPATH,xpath)

        for char in word:
            input_field.send_keys(char)
            time.sleep(speed)

    def type_and_enter(self,word,xpath,driver,speed=0.01):
        input_field = driver.find_element(By.XPATH,xpath)

        for char in word:
            input_field.send_keys(char)
            time.sleep(speed)

        input_field.send_keys(Keys.ENTER)

    def send_input(self,word,xpath,driver):
        input_field = driver.find_element(By.XPATH,xpath)
        input_field.send_keys(word)

    def send_and_enter(self,word,xpath,driver):
        input_field = driver.find_element(By.XPATH,xpath)
        input_field.send_keys(word)
        input_field.send_keys(Keys.ENTER)
    
    


