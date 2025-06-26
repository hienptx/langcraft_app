
# ✅ Goal

# Chain 1: Extract idioms → used in:

# Chain 2: Create matching exercise from idioms

# Chain 3: Evaluate user answers and give feedback

from langchain.prompts import ChatPromptTemplate, HumanMessagePromptTemplate

extract_prompt = ChatPromptTemplate.from_messages([
    HumanMessagePromptTemplate.from_template(
        """
        You will be given a text containing multiple German idioms. Each idiom includes:
        - An explanation in English (starting with 'Explanation:')
        - A translation in English (starting with 'Translation:')

        Your task is to extract only:
        - The **German idioms**
        - Their corresponding **explanations** (not translations)

        Return them as a numbered list in this format:

        1. [German idiom] – a. [English explanation]
        2. [German idiom] – b. [English explanation]

        ❗ Do NOT use the translation. Only use the line starting with "Explanation:".
        ❗ Do NOT include examples or extra commentary.
        ❗ Do NOT return anything else outside the list.

        Here is the text:

        {text}
        """
    )
])


matching_prompt = ChatPromptTemplate.from_messages([
    HumanMessagePromptTemplate.from_template(
   """
        Matching Exercise:
        Create a matching exercise for these German idioms and their meanings

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
        The German idioms should be numbered 1, 2, ... and the English explaination should be lettered a, b, ...
    """
    )
])

evaluate_matching_prompt = ChatPromptTemplate.from_messages([
    HumanMessagePromptTemplate.from_template(
        """
        From this exercise:
        {exercise}
        Evaluate the user's answer {user_answer}
        Instruction:

        - Validate if the matches are correct based on the idiom explanations.
        - Do not rely on translations; base correctness on the **explanation** text.

        Provide:
        - Correctness report
        - A brief explanation of any mismatch
        """
    )
])