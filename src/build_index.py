from document_loader import load_documents
from text_splitter import split_documents
from embedding_model import load_embedding_model
from vector_store import create_vector_store

docs = load_documents()

chunks = split_documents(docs)

embeddings = load_embedding_model()

create_vector_store(chunks, embeddings)

print("Vector Database Created Successfully")