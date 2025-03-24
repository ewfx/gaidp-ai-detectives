from data_ingestion import load_csv_instructions, load_transaction_data
from rule_generation import generate_profiling_rules
from rule_parsing import parse_rules
from rule_application import apply_rules
from remediation_action import generate_remediation_actions

def process_regulatory_data_profiling(instructions_file, transaction_file):
    # Load instructions
    instructions_data = load_csv_instructions(instructions_file)
    instructions_text = " ".join([doc.page_content for doc in instructions_data])
    
    # Generate rules
    rules_text = generate_profiling_rules(instructions_text)
    
    # Parse rules
    structured_rules = parse_rules(rules_text)
    
    # Load transactions
    transaction_data = load_transaction_data(transaction_file)
    
    # Apply rules
    violations = apply_rules(transaction_data, structured_rules)
    
    # Generate remediation
    remediation_actions = generate_remediation_actions(violations, structured_rules)
    
    return {
        'rules': rules_text,
        'structured_rules': structured_rules,
        'violations': violations,
        'remediation_actions': remediation_actions
    }
