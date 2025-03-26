from langchain_community.document_loaders import PyPDFLoader, CSVLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

# This code handles loading CSV instruction files and transaction data, 
# then splits large documents into manageable chunks using the RecursiveCharacterTextSplitter

file_path1 = "../artifacts/data/H1-Rule_set_Copy.csv"
file_path2 = "../artifacts/data/Large_Credit_Facility_Data__10k_rows_.csv"

# Load CSV instruction documents
def load_csv_instructions(file_path1):
    loader = CSVLoader(file_path1)
    data = loader.load()
    return data

print(file_path1)

# Load transaction data
def load_transaction_data(file_path2):
    import pandas as pd
    return pd.read_csv(file_path2)

# Split documents into chunks for processing
def split_documents(documents):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len,
    )
    return text_splitter.split_documents(documents)
