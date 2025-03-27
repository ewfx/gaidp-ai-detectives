# rule_application.py
import pandas as pd
import re

def apply_rules(transaction_df, structured_rules):
    """Apply parsed rules to transaction data"""
    violations = []
    
    for rule in structured_rules:
        try:
            violations += execute_rule_validation(transaction_df, rule)
        except Exception as e:
            violations.append({
                "rule_id": rule.get('rule_id', 'Unknown'),
                "error": f"Rule validation failed: {str(e)}"
            })
    
    return violations

def execute_rule_validation(df, rule):
    """Validate specific rule against dataframe"""
    field = rule['field']
    condition = rule['condition']
    v_type = rule['validation_type']
    
    if field not in df.columns:
        return [{
            "rule_id": rule['rule_id'],
            "field": field,
            "issue": "Field not found in dataset",
            "sample_data": None
        }]
    
    if v_type == 'format_check':
        return validate_format(df, field, condition, rule)
    elif v_type == 'value_range':
        return validate_value_range(df, field, condition, rule)
    elif v_type == 'consistency_check':
        return validate_consistency(df, field, condition, rule)
    else:
        return [{
            "rule_id": rule['rule_id'],
            "error": f"Unknown validation type: {v_type}"
        }]

def validate_format(df, field, pattern, rule):
    """Validate string format using regex"""
    pattern = re.compile(pattern)
    mask = df[field].astype(str).apply(lambda x: bool(pattern.match(x)))
    return get_violations(df[~mask], rule, f"Format mismatch: {pattern.pattern}")

def validate_value_range(df, field, range_str, rule):
    """Validate numerical ranges"""
    try:
        min_val, max_val = map(float, re.findall(r"\d+\.?\d*", range_str))
        mask = df[field].between(min_val, max_val)
        return get_violations(df[~mask], rule, f"Value outside {min_val}-{max_val}")
    except Exception as e:
        return [{
            "rule_id": rule['rule_id'],
            "error": f"Invalid range format: {str(e)}"
        }]

def get_violations(violation_df, rule, message):
    """Standard violation format"""
    if violation_df.empty:
        return []
    
    return [{
        "rule_id": rule['rule_id'],
        "field": rule['field'],
        "issue": message,
        "sample_data": violation_df.head(5).to_dict('records')
    }]
