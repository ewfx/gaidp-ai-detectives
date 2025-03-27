# main.py
import pandas as pd
from data_ingestion import load_csv_instructions, load_transaction_data
from rule_generation import generate_profiling_rules
from rule_parsing import parse_rules
from rule_application import apply_rules
from remediation_actions import generate_remediation_actions

# File paths should use raw strings (r prefix) or forward slashes to handle backslashes correctly
# file_path1 = r"C:\Users\phani\OneDrive\Desktop\Test\H1-Rule_Set _Copy.csv"
# file_path2 = r"C:\Users\phani\OneDrive\Desktop\Test\Large_Credit_Facility_Data__10k_rows_.csv"

# Alternative approaches:
# file_path1 = "C:/Users/phani/OneDrive/Desktop/Test/H1-Rule_Set _Copy.csv"
# file_path2 = "C:/Users/phani/OneDrive/Desktop/Test/Large_Credit_Facility_Data__10k_rows_.csv"

file_path1 = "./H1-Rule_Set_Copy.csv"
file_path2 = "./Large_Credit_Facility_Data__10k_rows_.csv"

def process_regulatory_data_profiling(file_path1, file_path2):
    """End-to-end processing pipeline"""
    # Data Loading
    instructions = load_csv_instructions(file_path1)
    instructions_text = " ".join([doc.page_content for doc in instructions])
    
    # Rule Generation & Parsing
    raw_rules = generate_profiling_rules(instructions_text)
    structured_rules = parse_rules(raw_rules)
    
    # Transaction Processing
    transactions = load_transaction_data(file_path2)
    violations = apply_rules(transactions, structured_rules)
    
    # Remediation Generation
    remediations = generate_remediation_actions(violations, structured_rules)
    
    return {
        "raw_rules": raw_rules,
        "structured_rules": structured_rules,
        "violations": violations,
        "remediation_actions": remediations
    }

if __name__ == "__main__":
    
    # Example Usage

    file_path1 = "./H1-Rule_Set_Copy.csv"
    file_path2 = "./Large_Credit_Facility_Data__10k_rows_.csv"

    results = process_regulatory_data_profiling(
        file_path1,
        file_path2
    )
    
    # Print formatted results
    print("Generated Rules:")
    print(results['raw_rules'])
    
    print("\nStructured Rules:")
    print(pd.DataFrame(results['structured_rules']))
    
    print("\nViolations Found:")
    for violation in results['violations']:
        print(f"{violation['rule_id']} - {violation['field']}: {violation['issue']}")
    
    print("\nRemediation Actions:")
    for remediation in results['remediation_actions']:
        print(f"{remediation['violation']['rule_id']}:")
        print(remediation['remediation'])
        print("="*50)
