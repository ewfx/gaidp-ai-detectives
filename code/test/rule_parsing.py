# rule_parsing.py
import re
import json
from openai import OpenAI
import config

client = OpenAI(api_key=config.Config.OPENAI_API_KEY)

def parse_rules(rules_text):
    """Parse generated rules into structured JSON format"""
    try:
        # First try direct JSON parsing
        return json.loads(rules_text)
    except json.JSONDecodeError:
        # Fallback to GPT structuring
        return structure_with_llm(rules_text)

def structure_with_llm(rules_text):
    """Use GPT to structure unstructured rules"""
    prompt = f"""
    Convert these data profiling rules into valid JSON format:
    
    {rules_text}
    
    Required JSON schema:
    {{
        "rules": [
            {{
                "rule_id": "string",
                "description": "string",
                "field": "string",
                "condition": "string",
                "validation_type": "string"
            }}
        ]
    }}
    """
    
    response = client.chat.completions.create(
        model="gpt-4-turbo",
        messages=[{"role": "user", "content": prompt}],
        response_format={"type": "json_object"},
        temperature=0.1
    )
    
    return json.loads(response.choices[0].message.content)["rules"]
