import time
import requests
import json

# Define the API endpoint
# api_url = "http://localhost:5000/books"  # Update the URL if necessary

# # Add a new book
# new_book = {
#     "title": "New Python Book",
#     "author": "Pythonista"
# }

# response = requests.post(api_url, json=new_book)

# if response.status_code == 201:
#     print("Book added successfully!")
# else:
#     print(f"Failed to add book. Status code: {response.status_code}")

# # Retrieve the list of books
# response = requests.get(api_url)

# if response.status_code == 200:
#     books = response.json()
#     print("List of books:")
#     for book in books:
#         print(f"Title: {book['title']}, Author: {book['author']}")
# else:
#     print(f"Failed to retrieve books. Status code: {response.status_code}")

q = input()
ai_url = 'http://localhost:5000/ai_chat'
question = q

ai_response = requests.post(ai_url, json=question)

if ai_response.status_code == 201:
    print("Question sent!")
else:
    print(f"Failed to add book. Status code: {ai_response.status_code}")

response =ai_response.content

print(response)