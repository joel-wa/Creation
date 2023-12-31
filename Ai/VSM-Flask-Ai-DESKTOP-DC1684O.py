from flask import Flask, request, jsonify
import replicate
from flask_cors import CORS

import os

os.environ['REPLICATE_API_TOKEN'] = "r8_WuzzeCxoclTjO8x6dRpLWKr9OUgX9RG1cNDiz"

# replicate_api_token: str = "r8_WuzzeCxoclTjO8x6dRpLWKr9OUgX9RG1cNDiz"
replicate_api_token = os.getenv("REPLICATE_API_TOKEN")

file_path = r"C:\\Users\\RanVic\\OneDrive\\Desktop\\System Prompt for VSM SAP.txt"  # Replace with your file path
with open(file_path, 'r') as file:
    # Read the entire file content into a variable
    file_contents = file.read()

system_prompts = file_contents

input_validators = [
    'add product',
    'remove product',
    'edit inventory',
    'largest country',
    'who is jesus christ',
    'smallest country',
]

validators = {
    'Add Product':'AddProductPage',
    'Remove Product':'InventoryPage',
    'Edit Inventory':'InventoryPage',
}


# Create the Flask app
app = Flask(__name__)

CORS(app)


def validate_input(input:str):
    value = input.lower()
    if value in input_validators:
        return True
    else:
        return False

# model = replicate.load("meta/llama-2-70b-chat")

def run_ai_13b(message):
    prompt = message
    output = replicate.run(
        "meta/codellama-13b:cc618fca92404570b9c10d1a4fb5321f4faff54a514189751ee8d6543db64c8f",
        input={"prompt":prompt,"system_prompt":system_prompts},
        api_token =os.environ['REPLICATE_API_TOKEN']
    )
    return output

@app.route('/',methods = ['GET'])
def ask_server():
    value = 'Hello'
    return value,201

@app.route('/aiReq',methods = ['GET'])
def ask_ai():
    data = 'a vintage color in RGB format, example (255,255,255) as white'
    output = run_ai_13b(data)
    return output,201


@app.route('/aiIMGgen',methods = ['POST'])
def request_image():
    data = request.get_json()

@app.route('/aiChat',methods = ['POST','GET'])
def request_ai():
    data = request.get_json()
    #Compare with validators to reduce AI cost
    # if(validate_input(data) == False):
    #     value =  jsonify({'response':'hello'})
    #     print(value)
    #     return value,201
    
    # #Begin ai
    output = run_ai_13b(data)
    # response = jsonify({'response':output})
    print(output)
    return output,201




if __name__ == '__main__':
    app.run()