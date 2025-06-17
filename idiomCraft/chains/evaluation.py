from langchain.prompts import PromptTemplate

evaluation_prompt = PromptTemplate(
    input_variables=["user_sentence", "idiom"],
    template="Evaluate this sentence: '{user_sentence}' using idiom '{idiom}'."
    "Grade the sentence from 1 to 10 according to your research"
    "Give constructive feedback in simple language, in 3 sentences."
)
