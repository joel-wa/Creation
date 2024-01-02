import json
import re
from flask import Flask, request, jsonify
import replicate
from flask_cors import CORS
import openai

#Utility Functions
def navFunc(json_data):
        # Parse the JSON data to extract the 'page' value
        data = json.loads(json_data)
        page = data.get('page', '')
        message = f'Tap the Button to go to {page}: [nav:{page}]'
        return message
    

def changeThemeFunc(json_data):
    # Parse the JSON data to extract theme_key and new_color
    data = json.loads(json_data)
    new_color = data.get('new_color', '')
    theme_key = data.get('theme_key', '')

    # Use regular expression to extract the RGB values from the new_color string
    rgb_values = re.findall(r'(\d+), (\d+), (\d+)', new_color)

    # Convert and add the RGB values to the list
    R,G,B = 0,0,0
    for r, g, b in rgb_values:
        R,G,B = int(r),int(g),int(b)
    
    message = f'You can change your {theme_key} by tapping on the below button [sm:changeTheme:{theme_key}:{R},{G},{B}]'
    print(f"\n\n\n {message} \n\n\n")
    return message

def modifySectionFunc(json_data):
    # Parse the JSON data to extract section_preset and section_index
    data = json.loads(json_data)
    section_preset = data.get('section_preset', '')
    section_index = data.get('section_index', -1)  # Default value if not present or not an integer
    message = f'Tap the Button below to change that section to {section_preset}. [sm:changeSection:{section_index}:{section_preset}]'
    print(f"\n\n\n {message} \n\n\n")
    return message

def makeShopFunc(json_data):
        data = json.loads(json_data)
        shopName = data.get('shopName','')
        shopCat = data.get('shopCat','')
        s1 = data.get('s1','')
        s2 = data.get('s2','')
        s3 = data.get('s3','')
        s4 = data.get('s4','')
        primaryColor = data.get('primaryColor','')
        secondaryColor = data.get('secondaryColor','')
        secondary2Color = data.get('secondary2','')
        accentColor = data.get('accentColor','')
        textColor = data.get('textColor','')
        neutralColor = data.get('neutralColor','')

        val = f"{shopName},{shopCat},{s1},{s2},{s3},{s4},{primaryColor},{secondaryColor},{accentColor},{neutralColor},{textColor}"


        message = f"'Shop Name': '{shopName}','Category': '{shopCat}','s1': '{s1}','s2': '{s2}','s3': '{s3}','s4': '{s4}','primary': '{primaryColor}','secondary': '{secondaryColor}','secondary2': '{secondary2Color}','accent': '{accentColor}','neutral': '{neutralColor}','text Color':'{textColor}',"
        

        return message



def parseAIResponse(response_message):
    if response_message.get("function_call"):
        function_name = response_message['function_call']['name']
        # print(function_name)
        #Save all the various function's arguments
        function_args = response_message["function_call"]["arguments"]
        # print("start")
        # print(function_args)
        # print("\n end")

        # match(function_name):
        if function_name == 'navigation':
            value = navFunc(function_args)
            return value
        elif function_name == 'changeTheme':
            print('doing')
            value = changeThemeFunc(function_args)
            return value
        elif  function_name == 'modify_section':
            value = modifySectionFunc(function_args)
            return value
        elif 'makeShop':
            value = makeShopFunc(function_args)
            return value
    else:
        message = response_message['content']
        return message



def get_ai(user_prompt):
    functions = [
  {
    "name":"navigation",
    "description":"navigate to a page",
    "parameters":{
        "type": "object",
        "properties":{
            "page":{"type":"string",
                    "description":"""The page a user wants to visit based on the descriptions: Dashboard: Gives access to Inventory Page (\"Inventory\"), Orders Page (\"Orders\"), and Shop Appearance Page (\"Shop Appearance\") in the form of Cards.Shop Orders: This allows one to manage new, completed, and historical orders.Inventory: This allows one to view, add/create (Create New Product Page), edit(Edit Product Page), or delete products from their Shop.Edit Product Page: Accessible only by selecting the product one wants to edit from the Inventory, and allows one to change the details of that product.Create New Product Page: This allows one to create and add a new product to their Inventory.Shop Appearance: Gives access to Shop Interface Edit Page, Shop Details Page, Shop Colors Page, Shop Filters Page.Shop Details Page: This allows one to set their Shop\'s banner image, logo image, shop name, and shop contact number. Select the \"save changes\" button below to save changes made.Shop Interface Edit Page: This page allows one to edit and manage the various sections of their shop\'s home page.Shop Colors Page: This page allows one to change their shop\'s Theme Colors.Shop Filters Page: This page allows one to create Filters for their shops."""},

          },
          "required":["page"],
    }
  },
  
   {
    "name":"changeTheme",
    "description":"""change the theme colors of the shop or app based on: The Primary Color is used as the default background color for all sections in the Shop.
The Secondary Color is used as the background color for the sticker on top of carousel products to show discounts. 
Secondary 2 is used for show the discount percentage of prices of products, Active Navigation Icon in Bottom navigation Bar.
The Accent Color is used for Call-To-Action buttons like the active state of the wishlist icon, "Add to Cart" button, and "Confirm Order" Button.
The Neutral Color is used to for inactive Icons in the Navigation bar, prices before discounts, dividers, etc.
The Text Color is used for the default text colors of titles of sections and since sections have a default background color of Primary Color, it should be in contrast with the primary color for easier readability.""",
 "parameters":{
        "type": "object",
        "properties":{
            "new_color":{
                "type":"string",
                "description":"corresponding color in rgb format, eg. for white is (255,255,255)"
            },
            "theme_key":{
                "type":"string",
                "description":"The specific theme color being changed",
                "enum":["primary","secondary","accent","secondary2","neutral","textColor"]
            }
        }
    },
    "required":["new_color","theme_key"]
},

  {
        "name":"modify_section",
        "description":"for changing one of the four sections of the layout structure of a user's layout or homepage",
        "parameters":{
            "type": "object",
            "properties":{
                "section_preset":{
                    "type":"string",
                    "description":"The type of preset to change the section to",
                    "enum":["Carousel","Grid","Horizonatal"]
                },
                "section_index":{
                    "type":"integer",
                    "description":"The Index of the Section being changed"
                }
            },
        },
        "required":["section_preset","section_index"]
    },

    {'name': 'makeShop', 'description': 'function to make a shop from start', 'parameters': {'type': 'object', 'properties': {'shopName': {'type': 'string', 'description': 'name of the shop'}, 'shopCat': {'type': 'string', 'description': 'type of products sold by the shop', 'enum': ['Fashion', 'Food']}, 's1': {'type': 'string', 'description': "first section of the Shop app's UI design, coming underneath the appBar or header.", 'enum': ['Carousel', 'Grid', 'HorizontalView']}, 's2': {'type': 'string', 'description': 'same as s1, but comes under s1', 'enum': ['Carousel', 'Grid', 'HorizontalView']}, 's3': {'type': 'string', 'description': 'same as s2, but comes under s2', 'enum': ['Carousel', 'Grid', 'HorizontalView']}, 's4': {'type': 'string', 'description': 'same as s3 but comes under s3', 'enum': ['Carousel', 'Grid', 'HorizontalView']}, 'primaryColor': {'type': 'string', 'description': 'primary color of the shop which serves as the default background color. should be in RGB format eg. white = 255,255,255'}, 'secondaryColor': {'type': 'string', 'description': 'secondary color of the shop app, should come in same format as primary color'}, 'secondary2': {'type': 'string', 'description': 'same format as primary color. serves as the color of Call to Actions and promo numbers on carousel products'}, 'accentColor': {'type': 'string', 'description': 'accent color of the shop. same format as primary color. serves as color of discount prices.'}, 'textColor': {'type': 'string', 'description': 'color of text which should contrast the primary color. should come in same format as primary color'}, 'neutralColor': {'type': 'string', 'description': 'same format as all the other colors. serves as color of inactive buttons or neutral elements like dividers etc.'}}}}

    ]

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-0613",
        messages = [{"role":"system","content":"You are a mobile app assistant chat bot"},{"role": "user", "content": user_prompt}],
        functions=functions,
        function_call="auto",  # auto is default, but we'll be explicit
    )
    response_message = parseAIResponse(response["choices"][0]["message"])
    print(response)
    return response_message


# Create the Flask app
app = Flask(__name__)

CORS(app)


@app.route('/aiChat',methods = ['POST','GET'])
def chat_ai():
    data = request.get_json()
    # data = 'I want an app to sell clothes, name it Joey and let it be classic like zara'
    output = get_ai(data)
    # response = jsonify({'response':output})
    print(output)
    return output,201



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)