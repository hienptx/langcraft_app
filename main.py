# fastapi app packages
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from pydantic import BaseModel

from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain_mistralai.chat_models import ChatMistralAI

from dotenv import load_dotenv
import os

app = FastAPI()
# Mount static files (CSS, JS, etc.)
app.mount("/static", StaticFiles(directory="./static"), name="static")

# Jinja2 template setup
templates = Jinja2Templates(directory="./templates")

# Load the .env file
load_dotenv()
# assign key from env to langchain/openai
# os.environ["MISTRAL_API_KEY"] = os.getenv("MISTRAL_API_KEY")
api_key = os.getenv("MISTRAL_API_KEY")
if api_key is None:
    raise EnvironmentError("MISTRAL_API_KEY not found in envionment")

from langchain.chat_models import init_chat_model
model = init_chat_model("mistral-small", model_provider="mistralai")



# Model & chains
llm = ChatMistralAI(api_key=api_key, model="mistral-small", temperature=0.7)

idiom_prompt = PromptTemplate(
    input_variables=["nbr_idioms", "topic", "level"],
    template =(
    "You are a creative German teacher. You generate German idioms according to a given topic for a given level.\n\n"
    "Provide {nbr_idioms} idioms about {topic} for level {level}"
    "Ask user to make an example with one of given idiom"
    )
)
evaluation_prompt = PromptTemplate(
    input_variables=["user_sentence", "idiom"],
    template="Evaluate this sentence: '{user_sentence}' using idiom '{idiom}'."
    "Grade the sentence from 1 to 10 according to your research"
    "Give constructive feedback in simple language, in 3 sentences."
)

idiom_chain = LLMChain(llm=llm, prompt=idiom_prompt)
eval_chain = LLMChain(llm=llm, prompt=evaluation_prompt)

class IdiomRequest(BaseModel):
    nbr_idioms: int
    topic: str
    level: str

class EvalRequest(BaseModel):
    user_sentence: str
    idiom: str

@app.post("/generate_idioms")
def generate_idioms(req: IdiomRequest):
    result = idiom_chain.run({
        "nbr_idioms": req.nbr_idioms,
        "topic": req.topic,
        "level": req.level
    })
    return {"idioms": result}

@app.post("/evaluate_sentence")
def evaluate(req: EvalRequest):
    feedback = eval_chain.run({
        "user_sentence": req.user_sentence,
        "idiom": req.idiom
    })
    return {"feedback": feedback}



@app.get("/", response_class=HTMLResponse)
async def read_index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})