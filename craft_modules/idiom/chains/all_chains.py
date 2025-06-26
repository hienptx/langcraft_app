
# graph TD
#     A[POST /idiom-craft/generate-idioms] --> B[idiom_prompt_chain]
#     B --> idiom_list

#     C[POST /idiom-craft/extract] --> D[extract_chain]
#     D --> idioms_extracted

#     E[POST /idiom-craft/matching] --> F[matching_chain]
#     F --> matching_task

#     G[POST /idiom-craft/evaluate] --> H[evaluate_chain]
#     H --> feedback

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_community.chat_message_histories import ChatMessageHistory
from .prompt_generate_idioms import idiom_prompt
from api.API_key import get_api_key

# Memory store
store = {}

class SessionWrapper:
    def __init__(self):
        self.history = ChatMessageHistory()
        self.meta = {}

    def add_user_message(self, msg):
        self.history.add_user_message(msg)

    def add_ai_message(self, msg):
        self.history.add_ai_message(msg)

def get_session_history(session_id: str) -> SessionWrapper:
    if session_id not in store:
        store[session_id] = SessionWrapper()
    return store[session_id]

# LLM setup
provider = "mistral"
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

from .prompt_matching_exercise import extract_prompt, matching_prompt, evaluate_matching_prompt
from .prompt_creative_task import extract_idioms_list_prompt, feedback_prompt
from .prompt_filling_task import filling_task_prompt
# Simple chains
extract_chain = extract_prompt | llm
matching_chain = matching_prompt | llm
evaluate_chain = evaluate_matching_prompt | llm

extract_idioms_chain = extract_idioms_list_prompt | llm
feedback_chain = feedback_prompt | llm

filling_gap_chain = filling_task_prompt | llm
