import boto3
import json
import numpy as np

# This converts the generated rules into a structured JSON format for easier application and management.

def parse_rules(rules_text):
    # Send to Titan model to structure the rules
    bedrock_client = boto3.client(service_name='bedrock-runtime')
    prompt = f"""
    Parse the following data profiling rules into a structured JSON format:
    
    {rules_text}
    
    Return a valid JSON array where each object has the following properties:
    - rule_id: The unique identifier for the rule
    - description: The rule description
    - field: The data field to check
    - condition: The condition or threshold to apply
    - validation_type: The type of validation (value_range, format_check, consistency_check, etc.)
    
    Example format:
    [
      {{
        "rule_id": "R001",
        "description": "Check customer ID format",
        "field": "customer_id",
        "condition": "Must match pattern CU-\\d{{6}}",
        "validation_type": "format_check"
      }},
      ...
    ]
    """
    
    body = json.dumps({
        "inputText": prompt,
        "textGenerationConfig": {
            "maxTokenCount": 2048,
            "temperature": 0.1,
            "topP": 0.9
        }
    })
    
    response = bedrock_client.invoke_model(
        body=body,
        modelId="amazon.titan-text-premier-v1:0"
    )
    
    response_body = json.loads(response.get('body').read())
    structured_rules_text = response_body.get('results')[0].get('outputText')
    
    # Extract the JSON part from the response
    import re
    json_match = re.search(r'\[.*\]', structured_rules_text, re.DOTALL)
    if json_match:
        try:
            return json.loads(json_match.group(0))
        except json.JSONDecodeError:
            # Fallback parsing if needed
            pass
    
    # Simple fallback parsing
    rules = []
    # Parsing logic here
    return rules
