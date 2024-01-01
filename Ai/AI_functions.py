import json
import re


class AIFunctions:
    
    def __init__(self) -> None:
        pass

    function_json_list = [
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


    ]

    def navFunc(json_data):
        # Parse the JSON data to extract the 'page' value
        data = json.loads(json_data)
        page = data.get('page', '')
        message = f'Tap the Button to go to {page}: [nav:{page}] \n'
        # print(message)
        return message
        

    def changeThemeFunc(json_data):
        # Parse the JSON data to extract theme_key and new_color
        data = json.loads(json_data)
        new_color = data.get('new_color', '')
        theme_key = data.get('theme_key', '')
        color_name = data.get('color_name','')

        # Use regular expression to extract the RGB values from the new_color string
        rgb_values = re.findall(r'(\d+), (\d+), (\d+)', new_color)

        # Convert and add the RGB values to the list
        R,G,B = 0,0,0
        for r, g, b in rgb_values:
            R,G,B = int(r),int(g),int(b)
        
        message = f'You can change your {theme_key} to {color_name} by tapping on the below button [sm:changeTheme:{theme_key}:{R},{G},{B}] \n'
        # print(f"\n\n\n {message} \n\n\n")
        return message

    def modifySectionFunc(json_data):
        # Parse the JSON data to extract section_preset and section_index
        data = json.loads(json_data)
        section_preset = data.get('section_preset', '')
        section_index = data.get('section_index', -1)  # Default value if not present or not an integer
        message = f'Tap the Button below to change that section to {section_preset}. [sm:changeSection:{section_index}:{section_preset}] \n'
        # print(f"\n\n\n {message} \n\n\n")
        return message
    
    def mchainFunc(json_data):
        # Parse the JSON data to extract section_preset and section_index
        data = json.loads(json_data)
        section_preset = data.get('chain', '')
        # section_index = data.get('section_index', -1)  # Default value if not present or not an integer
        message = f'Begin Chaining \n'
        # print(f"\n\n\n {message} \n\n\n")
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


        message = f"Shop Name: {shopName},Category: {shopCat},s1: {s1},s2: {s2},s3: {s3},s4: {s4},primary: {primaryColor},secondary: {secondaryColor},secondary2: {secondary2Color},accent: {accentColor},neutral: {neutralColor},text Color: {textColor},"
        

        return message

