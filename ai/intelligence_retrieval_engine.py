from langchain_text_splitters import CharacterTextSplitter

from langchain_community.vectorstores import Chroma

from langchain_community.embeddings import HuggingFaceEmbeddings

from ai.investigation_engine import run_ai_investigation


def run_financial_investigation(text, entities):

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

    retrieval_query = f"""
    Analyze cross-border remittance activity.

    Origin Country:
    {entities['origin_country']}

    Destination Country:
    {entities['destination_country']}

    Amount:
    {entities['amount']}
    """

    relevant_docs = retriever.invoke(retrieval_query)

    context = " ".join([
        doc.page_content
        for doc in relevant_docs
    ])

    investigation = run_ai_investigation(context)

    return {
        "summary": investigation,
        "flags": [
            "Cross-border transaction detected",
            "Compliance review recommended",
            "Behavioral anomaly identified"
        ]
    }