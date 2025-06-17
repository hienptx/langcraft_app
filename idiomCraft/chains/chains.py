from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_community.chat_message_histories import ChatMessageHistory
from .generate_idioms import idiom_prompt
from api.API_key import get_api_key

# Memory store
store = {}

def get_session_history(session_id: str) -> ChatMessageHistory:
    if session_id not in store:
        store[session_id] = ChatMessageHistory()
    return store[session_id]

# LLM setup
provider = "openai"
api_key = get_api_key(provider)

if provider == "mistral":
    from langchain_mistralai.chat_models import ChatMistralAI
    llm = ChatMistralAI(
        api_key=api_key,
        model="mistral-small",
        temperature=0.6)
elif provider == "openai":
    from langchain_openai import ChatOpenAI
    llm = ChatOpenAI(
        api_key=api_key,
        model="gpt-4.1-nano",
        base_url="https://openrouter.ai/api/v1",
        temperature=0.7)

# Input formatting - return the input for RunnableWithMessageHistory
def format_inputs(input_dict):
    return {
        "nbr_idioms": input_dict["nbr_idioms"],
        "topic": input_dict["topic"],
        "level": input_dict["level"],
        "input": input_dict  # Add this for RunnableWithMessageHistory
    }

# Base chain
idiom_chain = (
    RunnablePassthrough(func=format_inputs)
    | idiom_prompt
    | llm
)

from .matching_exercise import extract_prompt, matching_prompt, evaluate_matching_prompt

# Simple chains
extract_chain = extract_prompt | llm
matching_chain = matching_prompt | llm
evaluate_answer_chain = evaluate_matching_prompt | llm