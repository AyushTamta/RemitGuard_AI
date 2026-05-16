import os

from dotenv import load_dotenv

from langchain_google_genai import ChatGoogleGenerativeAI


load_dotenv()


def run_ai_investigation(context):

    llm = ChatGoogleGenerativeAI(
        model="gemini-1.5-flash",
        google_api_key=os.getenv("GOOGLE_API_KEY"),
        temperature=0.3
    )

    prompt = f"""
    You are an AI-powered AML and
    cross-border remittance investigation system.

    Analyze the following transaction data.

    Context:
    {context}

    Return:
    1. Risk Level
    2. Investigation Summary
    3. Compliance Flags
    4. Recommended Action
    """

    response = llm.invoke(prompt)

    return response.content