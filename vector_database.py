from langchain_community.document_loaders import PDFPlumberLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_ollama import OllamaEmbeddings
from langchain_community.vectorstores import FAISS

pdf_directory='pdf/'

def upload_pdf(file):
    with open(pdf_directory + file.name,"wb") as f:
        f.write(file.getbuffer())

def load_pdf(file_path):
    loader=PDFPlumberLoader(file_path)
    documnet=loader.load()
    return documnet

file_path="/workspaces/lawyer-chatbot/universal_declaration_of_human_rights.pdf"
documents=load_pdf(file_path)
print(len(documents))

def create_chunks(documents):
    text_splitter=RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
        add_start_index=True
    )
    text_chunks=text_splitter.split_documents(documents)
    return text_chunks

text_chunks=create_chunks(documents)
print("Chunks count",len(text_chunks))

ollama_model="deepseek-r1:1.5b"
def get_model(ollama_model):
    embeddings=OllamaEmbeddings(model=ollama_model)
    return embeddings

FAISS_DB_PATH="vectorstore/db_faiss"
faiss_db=FAISS.from_documents(text_chunks,get_model(ollama_model))
faiss_db.save_local(FAISS_DB_PATH)

