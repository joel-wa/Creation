import time
from flask import Flask, request, jsonify
import SeleniumScript as SS
import threading

import time
from selenium import webdriver
from urlMap import UrlMapClass as uMap


options = webdriver.ChromeOptions()
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36"
options.add_argument(f"user-agent={user_agent}")
options.add_argument("user-data-dir=C:\\Users\\RanVic\\AppData\\Local\\Google\\Chrome\\UD-selenium")




prompt = 'generate a color based of the mood of the sentence I give you'

app = Flask(__name__)

ssInit = False
counter = 0

ss = SS.SeleniumTask()

try:
    driver = webdriver.Chrome(options= options)
    driver.get(url = uMap.urlmap['google_bard'])
    ss.begin(driver)
except:
    print('nope')

response_lock = threading.Lock()
response = ''


@app.route('/ai',methods = ['POST'])
def send_query():
    data = request.get_json()
    ss.sendQuery(data,driver)
    time.sleep(15)
    new_response = ss.return_response(ss)

    # Acquire the lock before updating the response
    with response_lock:
        response = new_response

    return response, 201



@app.route('/ai',methods = ['GET'])
def get_answer():
    return jsonify(response)

def start():
    if(ssInit == False):
        driver = webdriver.Chrome(options= options)
        ssInit = True


if __name__ == '__main__':
    
    app.run(debug=True)
    
    
