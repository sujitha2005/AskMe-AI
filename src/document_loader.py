from pathlib import Path
from langchain_community.document_loaders import DirectoryLoader, TextLoader

def load_documents():

    data_path = Path(__file__).parent.parent / "data" / "documents"

    loader = DirectoryLoader(
        str(data_path),
        glob="*.txt",
        loader_cls=TextLoader
    )

    return loader.load()