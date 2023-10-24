import replicate
import os

replicate_api_token = os.getenv("REPLICATE_API_TOKEN")
# replicate_api_token: str = "r8_WYxUzEqqzbgVUgaPcBI1XIIOBcuGseA1wakWQ"

if replicate_api_token is None:
    raise ValueError("REPLICATE_API_TOKEN environment variable not set")


output = replicate.run(
    "meta/llama-2-70b-chat:02e509c789964a7ea8736978a43525956ef40397be9033abf9fd2badfe68c9e3",
    input={"prompt":"Which is the largest country in the world"},
    api_token = replicate_api_token
)
# The meta/llama-2-70b-chat model can stream output as it's running.
# The predict method returns an iterator, and you can iterate over that output.
for item in output:
    # https://replicate.com/meta/llama-2-70b-chat/versions/02e509c789964a7ea8736978a43525956ef40397be9033abf9fd2badfe68c9e3/api#output-schema
    print(item, end="")

answer = ''

for item in output:
    answer.ap