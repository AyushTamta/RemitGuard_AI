from langchain_community.llms import Ollama

def analyze_with_llm(text):

    llm = Ollama(model="llama3")

    prompt = f"""
    Analyze this banking document and detect fraud risk:

    Document:
    {text}

    Return:
    - Risk Level
    - Reason
    """

    response = llm.invoke(prompt)

    return response