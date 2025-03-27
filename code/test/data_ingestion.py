# data_ingestion.py
import pandas as pd
from langchain_community.document_loaders import CSVLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

def load_csv_instructions(file_path):
    """Load regulatory instructions from CSV with chunking"""
    loader = CSVLoader(file_path)
    print(loader.file_path)
    docs = loader.load()
    
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len
    )
    return splitter.split_documents(docs)

def load_transaction_data(file_path):
    """Load transaction data with pandas"""
    df = pd.read_csv(file_path)
    
    # Basic data cleaning
    df = df.convert_dtypes()
    df = df.dropna(how='all')
    
    return df
