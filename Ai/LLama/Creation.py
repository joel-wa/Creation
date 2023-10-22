from llama_cpp import Llama
import os
import os.path

dir = r"C:/Users/RanVic/Downloads/llama-2-7b-chat.ggmlv3.q8_0.bin"

LLM = Llama(model_path= "Ai\LLama\consolidated.00.pth")

# create a text prompt
prompt = "Q: What are the names of the days of the week? A:"

# generate a response (takes several seconds)
output = LLM(prompt)

# display the response
print(output["choices"][0]["text"])

