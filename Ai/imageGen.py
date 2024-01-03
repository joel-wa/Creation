import replicate
import os

os.environ["REPLICATE_API_TOKEN"] = "r8_WYxUzEqqzbgVUgaPcBI1XIIOBcuGseA1wakWQ" 

replicate_api_token = os.getenv("REPLICATE_API_TOKEN")
print(replicate_api_token)


output = ['https://replicate.delivery/pbxt/UyOIILoxrXpYNVdIcu03oDT4RxHTzlWPnwU0dN7Fq0NmJHiE/out-0.png']
# replicate.run(
#     "adirik/realvisxl-v3.0-turbo:6e941e7fe46955afc031f35e84312a792d546b0f434f9008d457eb9deb24575c",
#     input={"prompt": "An astronaut riding a rainbow unicorn"},
#     # api_token = replicate_api_token
# )
print(output[0])