from flask import Flask, request, jsonify
from flask_cors import CORS
import openai
import json
import re

openai.api_key = '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'

def requestAI(user_prompt):
    system_role = """hello and welcome,
If you own an online business or are considering starting one, this is the right place for you.
ChatGPt but for creating mobile apps.
With the VSM app, you can tell our AI the purpose of your app or give a short description, and within seconds, your app is ready. You can add your products, logo, brand image, contacts, and everything you need to get your app going and ready for business.
VSM is your all-in-one mobile app and shop creation platform. It empowers you to create a customized app effortlessly.
You can experience VSM by downloading our app. Give it a try to explore its features and simplicity.
Some of our features includes instant app access, and with this once your app is deployed, users new to you would not have to download your app which in turn reduces the friction of users purchasing from you.
End on a positive note: "Thank you for using VSM's Chatbot Assistant! If you have more questions or need assistance later, don't hesitate to reach out. Have a great day! 😊"""

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-0613",
        messages = [{"role":"system","content":system_role},
                    {"role": "user", "content": user_prompt}],
    )
    return response


# Create the Flask app
app = Flask(__name__)

CORS(app)

@app.route('/webChat',methods = ['POST','GET'])
def chatBot():
    data = 'What is VSM about'
    response = requestAI(data)
    print(response)
    return response,201



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)