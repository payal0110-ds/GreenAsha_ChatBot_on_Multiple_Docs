from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

def load_all_docs(paths):
    all_docs=[]
    for path in paths:
        loader=PyPDFLoader(path)
        all_docs.extend(loader.load())
    
    text_splitter=RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    text=text_splitter.split_documents(all_docs)
    return text

# paths=['Data/2024-12_CDR-Mission-MRV-Report.pdf','Data/Detailed Procedure for Compliance Mechanism.pdf',
#        'Data/ICAP offsets paper_vfin.pdf']
# result=load_all_docs(paths)
# print(result[-2])