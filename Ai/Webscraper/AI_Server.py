import time
from flask_cors import CORS
from selenium import webdriver
from flask import Flask, request, jsonify
from urlMap import UrlMapClass as uMap, XPaths
from elemenet_selector import Element_Selector as ES
from selenium.webdriver.common.by import By


# Create the Flask app
app = Flask(__name__)


CORS(app)

# Initialize the Chrome WebDriver (create it only once)
chrome_driver = None

response_data = "Hello, Flask and Chrome!"

def return_response(driver):
    values = driver.find_elements(By.XPATH,XPaths.xpaths['bard_answers'])
    answer = ''
    for value in values:
        answer += value.text
        answer +='\n'
    value_json = answer
    return value_json


def get_chrome_driver():
    global chrome_driver
    if chrome_driver is None:
        
        options = webdriver.ChromeOptions()
        user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36"
        options.add_argument(f"user-agent={user_agent}")
        options.add_argument("user-data-dir=C:\\Users\\RanVic\\AppData\\Local\\Google\\Chrome\\UD-selenium")
        chrome_driver = webdriver.Chrome(options=options)
    return chrome_driver

@app.route('/')
def index():
    # Get the Chrome WebDriver instance
    driver = get_chrome_driver()
    # Your code to interact with the WebDriver
    driver.get(uMap.urlmap['google_bard'])
    return response_data




@app.route('/ai',methods = ['POST'])
def send_ai_query():
    index()
    data = request.get_json()
    print("Posted")
    time.sleep(15)
    ES.send_and_enter(ES,data,XPaths.xpaths['bard_input'],chrome_driver)
    time.sleep(15)
    global response_data
    response_data = return_response(chrome_driver)
    print(response_data)
    return jsonify({'response': response_data}), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)
