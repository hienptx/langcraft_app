from langchain.prompts import ChatPromptTemplate, HumanMessagePromptTemplate

extract_prompt = ChatPromptTemplate.from_messages([
    HumanMessagePromptTemplate.from_template(
        """
        You will be given a text containing multiple German idioms with their translations, explanations, and examples.

        Your task is to extract only the German idioms and their English meanings from the text and return them as a numbered list in the format:

        1. [German idiom] – a. [English explaination]
        2. [German idiom] – b. [English explaination]


        Do NOT include any explanations, examples, or extra text.

        Here is the text:

        {text}
        """
    )
])


matching_prompt = ChatPromptTemplate.from_messages([
    HumanMessagePromptTemplate.from_template(
   """
        Create a matching exercise for these German idioms and their meanings:

        {idioms}

        Instructions:
        Format as two separate shuffled lists:

        **German Idioms:**
        1. [German idiom]
        ...

        **English explaination:**
        a. [English explaination]
        ...

        IMPORTANT: Shuffle both lists so the order doesn't match. 
        The German idioms should be numbered 1, 2, ... and the English meanings should be lettered a, b, ...

        {user_answer}
    """
    )
])

evaluate_matching_prompt = ChatPromptTemplate.from_messages([
    HumanMessagePromptTemplate.from_template(
        """
        Evaluate the user's answer: {user_answer}
        Instruction:
        - Check if the answer is correct.
        - Provide feedback on the correctness.
        """
    )
])