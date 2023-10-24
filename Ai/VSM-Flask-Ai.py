from flask import Flask, request, jsonify
import replicate
from flask_cors import CORS

import os

os.environ['REPLICATE_API_TOKEN'] = "r8_WuzzeCxoclTjO8x6dRpLWKr9OUgX9RG1cNDiz"

# replicate_api_token: str = "r8_WuzzeCxoclTjO8x6dRpLWKr9OUgX9RG1cNDiz"
replicate_api_token = os.getenv("REPLICATE_API_TOKEN")

system_prompts = 'If asked who Jesus is, your answer should be God'

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

def run_ai(message):
    output = replicate.run(
        "meta/llama-2-70b-chat:02e509c789964a7ea8736978a43525956ef40397be9033abf9fd2badfe68c9e3",
        input={"prompt":message},
        api_token =os.environ['REPLICATE_API_TOKEN']
    )
    return output

@app.route('/aiReq',methods = ['GET'])
def ask_ai():
    data = 'a vintage color in RGB format, example (255,255,255) as white'
    output = run_ai(data)
    return output,201


@app.route('/aiIMGgen',methods = ['POST'])
def request_image():
    data = request.get_json()

@app.route('/aiChat',methods = ['POST','GET'])
def request_ai():
    data = request.get_json()
    #Compare with validators to reduce AI cost
    if(validate_input(data) == False):
        value =  jsonify({'response':'hello'})
        print(value)
        return value,201
    
    # #Begin ai
    output = run_ai(data)
    # response = jsonify({'response':output})
    print(output)
    return output,201




if __name__ == '__main__':
    app.run()