from retriever import get_retriever


def answer_question(query):

    retriever = get_retriever()

    docs = retriever.invoke(query)

    context = "\n".join(
        doc.page_content for doc in docs
    )

    return context