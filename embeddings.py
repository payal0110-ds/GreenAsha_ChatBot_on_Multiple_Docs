from dataIngestion import load_all_docs

from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.vectorstores import FAISS

def create_embeddings():
    paths=['Data/2024-12_CDR-Mission-MRV-Report.pdf','Data/Detailed Procedure for Compliance Mechanism.pdf',
       'Data/ICAP offsets paper_vfin.pdf']
    docs = load_all_docs(paths)
    embeddings = (
        OllamaEmbeddings(model="gemma2:2b")
    )
    vectorStore = FAISS.from_documents(docs, embeddings)
    vectorStore.save_local("VectorDB/index")
    
create_embeddings()