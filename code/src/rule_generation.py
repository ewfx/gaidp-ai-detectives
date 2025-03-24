import boto3
import json
import numpy as np

# This function uses the Titan Foundation model to generate data profiling rules based on the provided regulatory instructions, 
# specifying the required fields, conditions, and validation types.

def generate_profiling_rules(instructions, model_id="amazon.titan-text-premier-v1:0"):
    bedrock_client = boto3.client(service_name='bedrock-runtime')
    
    prompt = f"""
    Based on the following regulatory reporting instructions, generate data profiling rules:
    
    {instructions}
    
    For each rule, provide:
    1. Rule ID
    2. Description
    3. Data field to check
    4. Condition or threshold
    5. Validation type (e.g., value range, format check, consistency check)
    """
    
    body = json.dumps({
        "inputText": prompt,
        "textGenerationConfig": {
            "maxTokenCount": 2048,
            "temperature": 0.2,
            "topP": 0.9
        }
    })
    
    response = bedrock_client.invoke_model(
        body=body,
        modelId=model_id
    )
    
    response_body = json.loads(response.get('body').read())
    generated_rules = response_body.get('results')[0].get('outputText')
    
    return generated_rules
