from langchain.llms import LlamaCpp
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler

MODEL_PATH ="C:\\Users\\RanVic\\Downloads\\llama-2-7b.Q5_0.gguf"

callback_manager = CallbackManager([StreamingStdOutCallbackHandler()])

def load_model() -> LlamaCpp:
    llm = LlamaCpp(
    model_path=MODEL_PATH,
    temperature=0.75,
    max_tokens=2000,
    top_p=1,
    callback_manager=callback_manager, 
    verbose=True, # Verbose is required to pass to the callback manager
    )
    return llm


prompt = 'Which country is the largest in the world?'

model = load_model()
model(prompt)