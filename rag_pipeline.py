import os
from pypdf import PdfReader
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_text_splitters import RecursiveCharacterTextSplitter

def build_vector_store(folder_path="Dataset"):
    full_text = ""

    for file in os.listdir(folder_path):
        if file.endswith(".pdf"):
            reader = PdfReader(os.path.join(folder_path, file))
            for page in reader.pages:
                text = page.extract_text()
                if text:
                    full_text += text + "\n"

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )

    docs = splitter.create_documents([full_text])

    embeddings = HuggingFaceEmbeddings()
    vectorstore = FAISS.from_documents(docs, embeddings)

    return vectorstore
