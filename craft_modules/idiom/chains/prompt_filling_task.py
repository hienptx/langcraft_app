from langchain.prompts import ChatPromptTemplate, HumanMessagePromptTemplate

filling_task_prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        "You are a helpful language tutor that creates fill-in-the-blank exercises using provided German idioms."
    ),
    HumanMessagePromptTemplate.from_template(
        """
            "Use the following list of German idioms: {idioms}.\n\n"
            "For each idiom:\n"
            "- Write a contextual sentence (or short paragraph) where the idiom fits naturally.\n"
            "- Replace the idiom in the sentence with a blank (e.g., '____').\n"
            "- After each sentence, include:\n"
            "  - Idiom: [the correct idiom]\n"
            "  - Translation: [idiom in English]\n"
            "  - Explanation: [simple explanation in English for learners at level {level}]\n\n"
            "Ensure the context makes it possible to guess the missing idiom from meaning or tone.\n"
            "Use CEFR level {level} (A1–C2) to guide vocabulary and sentence complexity."
        """    
    )
])