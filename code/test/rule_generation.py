# rule_generation.py
from openai import OpenAI
import config

client = OpenAI(api_key=config.Config.OPENAI_API_KEY)

def generate_profiling_rules(instructions_text):
    """Generate data profiling rules using GPT-4"""
    response = client.chat.completions.create(
        model="gpt-4-turbo",
        messages=[
            {
                "role": "system",
                "content": "You are a regulatory compliance expert specializing in financial data governance."
            },
            {
                "role": "user",
                "content": config.Config.INSTRUCTION_PROMPT.format(
                    instructions=instructions_text
                )
            }
        ],
        temperature=0.2,
        max_tokens=4000
    )
    return response.choices[0].message.content
