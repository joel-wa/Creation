from flask import Flask, request, jsonify
import replicate
from flask_cors import CORS
import openai

openai.api_key = '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'


def get_ai(user_prompt):
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
                }
            }
        },
        "required":["new_color"]
    },


    {
        "name":"modify_section",
        "description":"for changing one of the four sections of the layout structure of a user's layout or homepage",
        "parameters":{
            "type": "object",
            "properties":{
                "section_preset":{
                    "type":"string",
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
        messages = [{"role":"system","content":"You are a mobile app assistant chat bot"},{"role": "user", "content": user_prompt}],
        functions=functions,
        function_call="auto",  # auto is default, but we'll be explicit
    )
    response_message = response["choices"][0]["message"]
    print(response)
    return response_message


# Create the Flask app
app = Flask(__name__)

CORS(app)


@app.route('/aiChat',methods = ['POST','GET'])
def chat_ai():
    data = request.get_json()
    output = get_ai(data)
    # response = jsonify({'response':output})
    print(output)
    return output,201



if __name__ == '__main__':
    app.run()