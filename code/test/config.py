# config.py
import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    INSTRUCTION_PROMPT = """
    Analyze the following regulatory instructions and generate data profiling rules.
    Provide the rules in this exact format:
    
    Rule ID: [Unique identifier]
    Description: [Rule purpose]
    Field: [Data field to check]
    Condition: [Validation logic]
    Validation Type: [format_check|value_range|consistency_check]
    
    Instructions:
    {instructions}
    """
    
    REMEDIATION_PROMPT = """
    For this violation of {rule_description} on field '{field}':
    Violation Details: {violation_details}
    
    Generate remediation steps considering:
    1. Immediate data correction procedures
    2. Process improvements to prevent recurrence
    3. Regulatory compliance best practices
    """
