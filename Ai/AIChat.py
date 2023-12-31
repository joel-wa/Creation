import openai
import json
import csv



#Get Ai response Functions
def askAI_noChain(tools,messages):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-1106",
        messages=messages,
        tools=tools,
        tool_choice="auto",  # auto is default, but we'll be explicit
    )
    # print(response["choices"][0]["message"])
    response_message = response["choices"][0]["message"]
    return response_message

def askAI_chain(tools,messages):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-1106",
        messages=messages,
        tools=tools,
        tool_choice="auto",  # auto is default, but we'll be explicit
    )
    # print(response["choices"][0]["message"])
    response_message = response["choices"][0]["message"]
    return response_message

def load_from_csv(csv_filename):
    schema_list = []
    
    try:
        with open(csv_filename, mode='r') as file:
            reader = csv.reader(file)
            
            # Read header
            header = next(reader)
            
            # Ensure the header has the expected format
            if header == ["name", "description", "parameters"]:
                # Read data
                for row in reader:
                    function_name, function_description, parameters_str = row
                    
                    # Convert parameters from string to dictionary
                    parameters = eval(parameters_str)
                    
                    # Create schema and append to the list
                    schema = {
                        "name": function_name,
                        "description": function_description,
                        "parameters": parameters
                    }
                    schema_list.append(schema)
            else:
                print("Invalid CSV header format. Make sure the CSV file follows the expected format.")
    
    except FileNotFoundError:
        print(f"File not found: {csv_filename}")
    
    return schema_list

def parseAIResponse():
    pass

def process_user_input(user_input, data_store, chain_trigger=False):
    
    if chain_trigger:
        # Delete all data except the most recent entry
        data_store = [user_input]
    else:
        # Append the user input to the data store
        data_store.append(user_input)

    return data_store




def req_user_input():
    userInput = input('Ask a question: ')
    return userInput

function_file_name = 'test_CSV.csv'
function_list = load_from_csv(function_file_name)


chain= False
chatHistory = []


def run_convo():
    userInput = req_user_input()
    process_user_input(userInput,chatHistory,chain)
    # chatHistory = chat_data
    pass

while True:
    userIn = input('Do you want to ask a question y/n: ').lower()
    if userIn == 'y':
        run_convo()
    else:
        break

print(chatHistory)