import time
import json
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from urlMap import UrlMapClass as uMap
from urlMap import XPaths as XP
from elemenet_selector import Element_Selector as ES


class SeleniumTask:

    options = webdriver.ChromeOptions()
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36"
    options.add_argument(f"user-agent={user_agent}")
    options.add_argument("user-data-dir=C:\\Users\\RanVic\\AppData\\Local\\Google\\Chrome\\UD-selenium")


    driver_init = False

    prompt = 'generate a color based of the mood of the sentence I give you'


    def begin(self,driver:webdriver.Chrome) -> None:
        self.driver = driver
        self.driver.get(url = uMap.urlmap['google_bard'])
        self.driver_init = True
        try:
            
            time.sleep(5)
            ES.send_and_enter(ES,self.prompt,XP.xpaths['bard_input'],self.driver)
            time.sleep(15)
            values = self.driver.find_elements(By.XPATH,XP.xpaths['bard_answers'])

            answer = []
            for value in values:
                answer.append(value.text)
            value_json = answer
            print(value_json)

        except():
            print('no')


    def sendQuery(self,message,driver):
        ES.send_and_enter(ES,message,XP.xpaths['bard_input'],driver)

    def return_response(self):
        values = self.driver.find_elements(By.XPATH,XP.xpaths['bard_answers'])
        answer = []
        for value in values:
            answer.append(value.text)
        value_json = answer
        return value_json
    
    def end_script(self):
        self.driver.quit()







