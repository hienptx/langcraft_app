from langchain.prompts import ChatPromptTemplate, HumanMessagePromptTemplate

extract_idioms_list_prompt = ChatPromptTemplate.from_messages([
    HumanMessagePromptTemplate.from_template(
        """
        Get idioms list:
        You will be given a text containing multiple German idioms. Each idiom includes:
        - An explanation in English (starting with 'Explanation:')

        Your task is to extract only:
        - The **German idioms**

        Return them as a numbered list in this format:

        1. [German idiom]
        2. [German idiom]

        Here is the text:

        {text}

        [IMPORTANT]
        - Do not provide any extra texts except returning the list
        """
    )

])

feedback_prompt = ChatPromptTemplate.from_messages([
    ("system", "you are a creative, fair language assistant."),
    HumanMessagePromptTemplate.from_template(
        """
        From these idioms {idioms}
        You will grade and give feedback to this {text}
        Instructions:

        - Grade base on your language knowleadge
        - Fair and concise feedback
        - Provide a simple example
        """
    )
])