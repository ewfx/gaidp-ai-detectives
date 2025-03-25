
# This function applies the structured rules to the transaction data and identifies violations, 
# capturing the specific issues and sample data for remediation.

def apply_rules(transaction_data, structured_rules):
    violations = []
    
    for rule in structured_rules:
        rule_id = rule.get('rule_id')
        field = rule.get('field')
        condition = rule.get('condition')
        validation_type = rule.get('validation_type')
        
        # Check if field exists
        if field not in transaction_data.columns:
            violations.append({
                'rule_id': rule_id,
                'field': field,
                'issue': 'Field does not exist in the dataset',
                'sample_data': None
            })
            continue
        
        # Apply different checks based on validation type
        if validation_type == 'value_range':
            # Extract min and max values from condition
            import re
            range_match = re.search(r'between\s+(\d+(?:\.\d+)?)\s+and\s+(\d+(?:\.\d+)?)', condition, re.IGNORECASE)
            if range_match:
                min_val = float(range_match.group(1))
                max_val = float(range_match.group(2))
                
                # Check for violations
                mask = (transaction_data[field] < min_val) | (transaction_data[field] > max_val)
                if mask.any():
                    sample_violations = transaction_data.loc[mask].head(5)
                    violations.append({
                        'rule_id': rule_id,
                        'field': field,
                        'issue': f'Values outside range {min_val} to {max_val}',
                        'sample_data': sample_violations[field].tolist()
                    })
        
        elif validation_type == 'format_check':
            # Use regex pattern in condition
            pattern_match = re.search(r'pattern\s+(.*)', condition, re.IGNORECASE)
            if pattern_match:
                pattern = pattern_match.group(1).strip('"\'')
                
                # Check for violations using regex
                mask = ~transaction_data[field].astype(str).str.match(pattern)
                if mask.any():
                    sample_violations = transaction_data.loc[mask].head(5)
                    violations.append({
                        'rule_id': rule_id,
                        'field': field,
                        'issue': f'Values do not match pattern {pattern}',
                        'sample_data': sample_violations[field].tolist()
                    })
        
        # Add more validation types as needed
        
    return violations
