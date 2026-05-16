from langchain_community.llms import Ollama
from langchain_text_splitters import CharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings


def run_rag(text):

    splitter = CharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )

    docs = splitter.split_text(text)

    embeddings = HuggingFaceEmbeddings()

    vectorstore = Chroma.from_texts(
        docs,
        embeddings
    )

    retriever = vectorstore.as_retriever()

    llm = Ollama(model="llama3")

    query = """
    You are a banking fraud detection AI.

    Analyze this document and return:

    Risk Level: Low/Medium/High
    Risk Score: 1-100
    Reason:
    Recommended Action:
    """

    relevant_docs = retriever.invoke(query)

    context = " ".join([doc.page_content for doc in relevant_docs])

    prompt = f"""
    Context:
    {context}

    {query}
    """

    response = llm.invoke(prompt)

    return response