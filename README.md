#  AI Research Paper Summarizer

An AI-powered web application that summarizes research papers in student-friendly language by extracting key insights such as the problem statement, methodology, dataset, results, and limitations from PDF files.  
The system uses LLMs with Retrieval-Augmented Generation (RAG) to reduce paper reading and idea exploration time.

##  Features

- Upload research paper PDFs
- Automatically extract text from PDFs
- Generate structured summaries including:
  - Problem
  - Method
  - Dataset
  - Results
  - Limitations
- RAG-based pipeline for scalable document understanding
- Simple and interactive web interface using Streamlit

##  How It Works (Pipeline)

1. PDF Upload – User uploads a research paper in PDF format  
2. Text Extraction – PyPDF extracts text page-by-page  
3. Text Chunking – Long text is split into overlapping chunks  
4. Embeddings Generation – Text chunks are converted into vectors  
5. Vector Storage – FAISS stores embeddings for retrieval  
6. LLM Summarization – LLaMA 3.1 (via Groq) generates structured summaries  
7. UI Display– Summary is displayed using Streamlit  



##  Tech Stack

- Programming Language: Python  
- LLM Framework: LangChain  
- Language Model: LLaMA 3.1 (via Groq)  
- Inference Platform: Groq  
- NLP Concepts:Text summarization, chunking  
- RAG:Retrieval-Augmented Generation  
- Vector Database:FAISS  
- Embeddings:HuggingFace Embeddings  
- PDF Processing:PyPDF  
- Frontend:Streamlit  
- Version Control: GitHub  



##  Project Structure

AI-Research-Paper-Summarizer/

-app.py # Streamlit frontend
-pdf_loader.py # PDF text extraction
-summarizer.py # LLM-based summarization
-rag_pipeline.py # RAG vector store creation
-Dataset/ # Research paper PDFs
-requirements.txt


