import os
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate

llm = ChatGroq(
    model="llama-3.1-8b-instant",
    api_key=os.getenv("GROQ_API_KEY")
)

def summarize_paper(text):
    prompt = PromptTemplate(
        input_variables=["paper"],
        template="""
        Summarize the research paper in simple student-friendly language.
        Extract:
        1. Problem
        2. Method
        3. Dataset
        4. Results
        5. Limitations

        Paper:
        {paper}
        """
    )

    response = llm.invoke(prompt.format(paper=text[:6000]))
    return response.content
