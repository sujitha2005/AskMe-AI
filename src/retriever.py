from langchain_community.vectorstores import FAISS
from embedding_model import load_embedding_model


def get_retriever():

    embeddings = load_embedding_model()

    db = FAISS.load_local(
        "vectorstore",
        embeddings,
        allow_dangerous_deserialization=True
    )

    return db.as_retriever(
        search_kwargs={"k": 3}
    )