import faiss
from langchain_community.vectorstores import FAISS
from langchain_community.docstore.in_memory import InMemoryDocstore

# Facebook AI Similarity Search (FAISS) is used as the vector database for efficient similarity search and retrieval 
# of regulatory instructions. This helps in finding similar instructions and ensuring consistency in rule generation

def setup_vector_store(embeddings_model):
    # Initialize FAISS index
    dimension = 1024  # Dimension of Titan Text Embeddings
    index = faiss.IndexFlatL2(dimension)
    
    # Set up the vector store
    vector_store = FAISS(
        embedding_function=embeddings_model.get_embedding,
        index=index,
        docstore=InMemoryDocstore(),
        index_to_docstore_id={}
    )
    
    return vector_store

def add_documents_to_store(vector_store, documents):
    # Add documents to the vector store
    texts = [doc.page_content for doc in documents]
    embeddings = [vector_store.embedding_function(text) for text in texts]
    vector_store.add_embeddings(texts, embeddings, documents)
    return vector_store
