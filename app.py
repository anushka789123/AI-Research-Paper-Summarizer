import streamlit as st
from pdf_loader import extract_text_from_pdf
from summarizer import summarize_paper
from rag_pipeline import build_vector_store

st.set_page_config(
    page_title="AI Research Paper Summarizer",
    page_icon="📄",
    layout="centered"
)

st.markdown(
    """
    <h1 style='text-align:center;'>📄 AI Research Paper Summarizer</h1>
    <p style='text-align:center; color:gray;'>
    Upload a research paper PDF and get a quick summary with key insights
    </p>
    <hr>
    """,
    unsafe_allow_html=True
)

uploaded_file = st.file_uploader(
    "📤 Upload Research Paper (PDF)",
    type=["pdf"]
)

if uploaded_file:
    st.info("📘 Paper uploaded successfully")

    with st.spinner("🔍 Reading and analyzing the paper..."):
        text = extract_text_from_pdf(uploaded_file)
        summary = summarize_paper(text)

    st.success("✅ Analysis completed")

    st.subheader("🧠 Paper Summary")
    st.write(summary)

    st.markdown("---")
    st.caption("⚡ Built using Streamlit, LangChain, Llama 3.2 & RAG")

else:
    st.warning("👆 Please upload a research paper PDF to start")

