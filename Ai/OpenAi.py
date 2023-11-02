import openai
import json
from AI_functions import AIFunctions as af


import os

# os.environ['OPEN_AI_KEY'] = "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"
openai.api_key = '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'

# Example dummy function hard coded to return the same weather
# In production, this could be your backend API or an external API
def get_current_weather(location, unit="fahrenheit"):
    """Get the current weather in a given location"""
    weather_info = {
        "location": location,
        "temperature": "72",
        "unit": unit,
        "forecast": ["sunny", "windy"],
    }
    return json.dumps(weather_info)

def run_conversation():
    user_prompt = "change my CTA button color to light blue"
    # Step 1: send the conversation and available functions to GPT
    messages = [{"role":"system","content":"You are a mobile app assistant chat bot"},{"role": "user", "content": user_prompt}]
    functions = [
  {
    "name":"navigation",
    "description":"navigate to a page",
    "parameters":{
        "type": "object",
        "properties":{
            "page":{"type":"string","description":"""The page a user wants to visit based on the descriptions: Dashboard: Gives access to Inventory Page (\"Inventory\"), Orders Page (\"Orders\"), and Shop Appearance Page (\"Shop Appearance\") in the form of Cards.Shop Orders: This allows one to manage new, completed, and historical orders.Inventory: This allows one to view, add/create (Create New Product Page), edit(Edit Product Page), or delete products from their Shop.Edit Product Page: Accessible only by selecting the product one wants to edit from the Inventory, and allows one to change the details of that product.Create New Product Page: This allows one to create and add a new product to their Inventory.Shop Appearance: Gives access to Shop Interface Edit Page, Shop Details Page, Shop Colors Page, Shop Filters Page.Shop Details Page: This allows one to set their Shop\'s banner image, logo image, shop name, and shop contact number. Select the \"save changes\" button below to save changes made.Shop Interface Edit Page: This page allows one to edit and manage the various sections of their shop\'s home page.Shop Colors Page: This page allows one to change their shop\'s Theme Colors.Shop Filters Page: This page allows one to create Filters for their shops."""},
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
                    "enum":["primary","secondary","accent","secondary2","neutral","textColor"]
                }
            }
        },
        "required":["new_color","theme_key"]
    },



{
    "name":"modify_section",
    "description":"for changing the layout structure of a user's layout or homepage",
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

  ]
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-0613",
        messages=messages,
        functions=functions,
        function_call="auto",  # auto is default, but we'll be explicit
    )
    # print(response["choices"][0]["message"])
    response_message = response["choices"][0]["message"]
    print(response_message)
    return parseAIResponse(response_message)

    # Step 2: check if GPT wanted to call a function
    if response_message.get("function_call"):
        # Step 3: call the function
        # Note: the JSON response may not always be valid; be sure to handle errors
        available_functions = {
            "get_current_weather": get_current_weather,
        }  # only one function in this example, but you can have multiple
        function_name = response_message["function_call"]["name"]
        function_to_call = available_functions[function_name]
        function_args = json.loads(response_message["function_call"]["arguments"])
        function_response = function_to_call(
            location=function_args.get("location"),
            unit=function_args.get("unit"),
        )

        # Step 4: send the info on the function call and function response to GPT
        messages.append(response_message)  # extend conversation with assistant's reply
        messages.append(
            {
                "role": "function",
                "name": function_name,
                "content": function_response,
            }
        )  # extend conversation with function response
        second_response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo-0613",
            messages=messages,
        )  # get a new response from GPT where it can see the function response
        return second_response

def parseAIResponse(response_message):
    if response_message.get("function_call"):
        function_name = response_message['function_call']['name']
        print(function_name)
        #Save all the various function's arguments
        function_args = response_message["function_call"]["arguments"]
        print("start")
        print(function_args)
        print("\n end")

        match(function_name):
            case 'navigation':
                af.navFunc(function_args)
                return
            case 'changeTheme':
                print('doing')
                value = af.changeThemeFunc(function_args)
                return value
            case 'modify_section':
                af.modifySectionFunc(function_args)
                return




run_conversation()
# print()