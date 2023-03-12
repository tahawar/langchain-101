from dotenv import load_dotenv
from langchain.prompts import PromptTemplate
from langchain.llms import OpenAI
from langchain.chains import LLMChain
import os

# cargamos openai api key
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY

llm = OpenAI(temperature=0.9)

prompt = PromptTemplate(
    input_variables=["name"],
    template="Hola cómo estás? mi nombre es {name}",
)

# creamos una chain y le entregamos como parámetro el modelo y el prompt template
chain = LLMChain(llm=llm, prompt=prompt)

# ejecutamos la cadena con el parametro name = Fernando
print(chain.run("Fernando"))
