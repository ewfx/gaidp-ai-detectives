# remediation_actions.py
from openai import OpenAI
import config

client = OpenAI(api_key=config.Config.OPENAI_API_KEY)

def generate_remediation_actions(violations, structured_rules):
    """Generate AI-powered remediation steps"""
    remediations = []
    
    for violation in violations:
        rule = next(
            (r for r in structured_rules if r['rule_id'] == violation['rule_id']),
            None
        )
        
        if not rule:
            continue
            
        prompt = config.Config.REMEDIATION_PROMPT.format(
            rule_description=rule['description'],
            field=violation['field'],
            violation_details=violation['issue']
        )
        
        response = client.chat.completions.create(
            model="gpt-4-turbo",
            messages=[
                {"role": "system", "content": "You are a financial compliance consultant"},
                {"role": "user", "content": prompt}
            ],
            temperature=0.3,
            max_tokens=500
        )
        
        remediations.append({
            "violation": violation,
            "remediation": response.choices[0].message.content
        })
    
    return remediations
