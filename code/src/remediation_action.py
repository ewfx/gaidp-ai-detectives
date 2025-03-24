import boto3
import json
import numpy as np

# This uses the Titan Foundation model to generate detailed remediation actions for each violation, 
# providing step-by-step instructions for fixing data issues and preventing future violations.

def generate_remediation_actions(violations, structured_rules):
    bedrock_client = boto3.client(service_name='bedrock-runtime')
    remediation_actions = []
    
    for violation in violations:
        rule_id = violation['rule_id']
        field = violation['field']
        issue = violation['issue']
        sample_data = violation['sample_data']
        
        # Find the corresponding rule
        rule = next((r for r in structured_rules if r['rule_id'] == rule_id), None)
        
        if not rule:
            continue
        
        # Create prompt for remediation
        prompt = f"""
        For the following regulatory data profiling violation, suggest detailed remediation steps:
        
        Rule ID: {rule_id}
        Rule Description: {rule.get('description', 'No description available')}
        Field: {field}
        Issue: {issue}
        Sample Violating Data: {sample_data}
        
        Provide step-by-step remediation instructions that comply with banking regulations. Include both technical steps for fixing the data and process recommendations to prevent future violations.
        """
        
        body = json.dumps({
            "inputText": prompt,
            "textGenerationConfig": {
                "maxTokenCount": 1024,
                "temperature": 0.2,
                "topP": 0.9
            }
        })
        
        response = bedrock_client.invoke_model(
            body=body,
            modelId="amazon.titan-text-premier-v1:0"
        )
        
        response_body = json.loads(response.get('body').read())
        remediation = response_body.get('results')[0].get('outputText')
        
        remediation_actions.append({
            'violation': violation,
            'rule': rule,
            'remediation': remediation
        })
    
    return remediation_actions
