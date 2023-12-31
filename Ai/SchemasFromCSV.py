import csv

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

# Example usage
csv_filename = input("Enter the CSV filename to load: ")
loaded_schemas = load_from_csv(csv_filename)

# Print loaded schemas for verification
# for schema in loaded_schemas:
#     print(schema)
#     print(',')
print(loaded_schemas)