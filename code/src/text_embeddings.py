import boto3
import json
import numpy as np

# This class provides methods to generate embeddings using the Titan Text Embedding model, 
# which converts regulatory text into numerical representations for semantic understanding

class TitanEmbeddings:
    def __init__(self, model_id="amazon.titan-embed-text-v2:0"):
        self.model_id = model_id
        self.bedrock_client = boto3.client(service_name='bedrock-runtime')
        
    def get_embedding(self, text, dimensions=1024, normalize=True):
        body = json.dumps({
            "inputText": text,
            "dimensions": dimensions,
            "normalize": normalize
        })
        
        response = self.bedrock_client.invoke_model(
            body=body,
            modelId=self.model_id
        )
        
        response_body = json.loads(response.get('body').read())
        embedding = response_body.get('embedding')
        return embedding
    
    def get_embeddings(self, texts, dimensions=1024, normalize=True):
        return [self.get_embedding(text, dimensions, normalize) for text in texts]
