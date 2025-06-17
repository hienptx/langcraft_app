

from langchain.prompts import ChatPromptTemplate, HumanMessagePromptTemplate

idiom_prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        "You are a helpful language tutor that explains idioms clearly for learners."
    ),
    (
        "human",
        (
            "Give me {nbr_idioms} German idioms on the topic \"{topic}\", suitable for level {level}.\n"
            "Write each idiom followed by:\n"
            "- A short explanation in simple English\n"
            "- An English translation\n"
            
            "Format like this:\n"
            "1. [Idiom]\n"
            "Translation: ...\n"
            "Explanation: ...\n\n"
        )
    )
])