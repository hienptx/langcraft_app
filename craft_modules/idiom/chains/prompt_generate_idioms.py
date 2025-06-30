from langchain.prompts import ChatPromptTemplate, HumanMessagePromptTemplate

idiom_prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        "You are a helpful language tutor that explains idioms clearly for learners."
    ),
    (
        "human",
        (
            "Give me {nbr_idioms} German idioms on the topic \"{topic}\", suitable for level {level} "
            "(where level can be A1, A2, B1, B2, C1, or C2 — corresponding roughly to beginner to advanced).\n"
            "Write each idiom followed by:\n"
            "- A contextual and simple explanation in English\n"
            "- An English translation\n"
            
            "Format like this:\n"
            "1. [Idiom]\n"
            "Explanation: ...\n\n"
            "Translation: ...\n"
        )
    )
])