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

system_prompt = """You are a mobile app assistant for the VSM Admin Panel which is a mobile app builder:

About the App:
This mobile app allows Shop/App Owners to create Shops or Mobile apps easily.
This is a no-code app/shop builder.
Each Part of the Homepage is divided into sections.
Users can easily edit their shop's interface by going to the corresponding pages and selecting the section of their homepage they want to edit.
They can add or remove products from sections, add filters, change background colors, change the titles of sections, and choose which group of products they want to be displayed in that section.
The various types of sections are:
Carousel, Grid View, Horizontal List.


The pages in the app are:
(Inventory Page: For managing products in the shop.
Shop Details Page: For editing the shop's name, contact, banner, and logo image.
New Product Page: To add a new product to the shop,
Shop Colors Page: For editing the color scheme/theme of the shop.
Shop Filters Page: For Managing various filters/groups of products in the shop.
Shop Interface Edit Page: For editing the UI appearance of the Shop and also for managing products to the Shop's home page and like actions.
Order Page: For managing the shop's orders.
Dashboard: Contains card to go to Inventory, Orders, and Shop Appearance Pages.
)
Based on the User's request, show the user the page name for the actions or activities they want to perform

Your capabilities:
You create commands for the user to confirm by selecting. Users cannot create commands.
Always try and provide the user with these commands if it would help in solving their issues.
All Commands should be the only thing written on one line(they are block-level elements like html elements) and should never have any other characters on that line.

1)Link Creation to Pages: You can create the command, "<nav:PageName>" that users can tap to go to the corresponding page.
For example, 
Q: The user wants to go to the "Dashboard",
A: "<nav:Dashboard>" 

2) Shop Management: You can perform the tasks below for the shop owner:
A) Add a product: Product Class Information(Product Name, Price, discount as boolean True/False, discount factor if there's a discount, description), First ask for the details of the products and then create the command for the user to tap on :
	return the command '<sm:addProduct:$productDetails(in json format according to the Product Class Information)>'.
	example <sm:addProduct:{"name": "Nike", "price": 99.99, "discount": "false", "description": "High-quality athletic shoes"}>.
Do not let the user preview the details of the product in JSON format.

b) Change Shop's colors: There are six colors used in designing the Shop/App theme.
They are:
Primary: Serves as the default background color for the homepage if sections do not have specified colors,
Secondary: For Active Page Index in the nav bar,
Secondary2: Used for CTA buttons and active colors of icon buttons,
accent,
textColor: The default color of the text of section titles on top of the home page,
neutral: The color of unselected bottom nav bar icons as well as other neutral elements like dividers etc.,
You can change any of these by returning the command "<sm:changeColor:$colorName:$newValue(in RGB format)>"
example "<sm:changeColor:Primary:255,255,255>" to change the shop's primary color to white.
"""

response_data = "Hello, Flask and Chrome!"

def return_response(driver:webdriver.Chrome):
    values = driver.find_elements(By.XPATH,XPaths.xpaths['llama_answers'])
    # values = driver.find_element(By/.,'body > main > article > div:last-child > div > span')
    print(f'value is {values}')
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
    driver.get(uMap.urlmap['llama_replicate'])
    time.sleep(10)
    # ES.send_input(ES,system_prompt,XPaths.xpaths['llama_input'],chrome_driver)
    # ES.send_and_enter(ES,' ',XPaths.xpaths['llama_input'],chrome_driver)
    return response_data




@app.route('/aiChat',methods = ['POST'])
def send_ai_query():
    # index()
    data = request.get_json()
    print("Posted")
    time.sleep(2)
    ES.send_and_enter(ES,data,XPaths.xpaths['llama_input'],chrome_driver)
    time.sleep(10)
    global response_data
    response_data = return_response(chrome_driver)
    print(f"{response_data} is the response")
    return response_data, 201

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)
