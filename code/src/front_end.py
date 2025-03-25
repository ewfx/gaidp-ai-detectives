import streamlit as st
import pandas as pd
import requests
import json
import boto3
from requests_aws4auth import AWS4Auth
import os

# This Streamlit application provides a user-friendly interface for uploading instruction and transaction files, 
# visualizing generated rules, and reviewing violations and remediation actions

st.set_page_config(page_title="Regulatory Data Profiling Assistant", layout="wide")

st.title("Regulatory Data Profiling Assistant")
st.markdown("### Automated data profiling for regulatory compliance")

# File upload section
col1, col2 = st.columns(2)

with col1:
    st.header("1. Upload Regulatory Instructions")
    instructions_file = st.file_uploader("Upload instructions CSV file", type=["csv"])
    
    if instructions_file:
        instructions_df = pd.read_csv(instructions_file)
        st.write("Preview of instructions:")
        st.dataframe(instructions_df.head())

with col2:
    st.header("2. Upload Transaction Data")
    transaction_file = st.file_uploader("Upload transaction data CSV file", type=["csv"])
    
    if transaction_file:
        transaction_df = pd.read_csv(transaction_file)
        st.write("Preview of transaction data:")
        st.dataframe(transaction_df.head())

# Process button
if st.button("Generate Rules and Remediation Actions") and instructions_file and transaction_file:
    with st.spinner("Processing your data..."):
        # Save files to temporary location
        with open("temp_instructions.csv", "wb") as f:
            f.write(instructions_file.getbuffer())
        
        with open("temp_transactions.csv", "wb") as f:
            f.write(transaction_file.getbuffer())
        
        # Upload files to S3
        s3_client = boto3.client('s3')
        bucket_name = 'genaidetectives'  # Replace with your bucket name
        
        s3_client.upload_file("temp_instructions.csv", bucket_name, "instructions.csv")
        s3_client.upload_file("temp_transactions.csv", bucket_name, "transactions.csv")
        
        # Call API Gateway endpoint
        api_url = "https://kz8vyrawe3.execute-api.us-east-1.amazonaws.com/dev/"
        
        # Get AWS credentials from boto3 session
        credentials = boto3.Session().get_credentials()
        region = 'us-east-1'

        # Create AWS4Auth instance
        auth = AWS4Auth(
            credentials.access_key,
            credentials.secret_key,
            region,
            'execute-api',
            session_token=credentials.token
        )

        payload = {
            "instructions_file": "instructions.csv",
            "transaction_file": "transactions.csv"
        }
        
        response = requests.post(api_url, json=payload)
        
        if response.status_code == 200:
            result = response.json()
            
            # Display tabs for different result sections
            tab1, tab2, tab3 = st.tabs(["Generated Rules", "Violations", "Remediation Actions"])
            
            with tab1:
                st.header("Generated Profiling Rules")
                st.text_area("Rules", result['rules'], height=300)
                
                # Display structured rules in a table
                st.subheader("Structured Rules")
                rules_df = pd.DataFrame(result.get('structured_rules', []))
                st.dataframe(rules_df)
            
            with tab2:
                st.header("Violations Detected")
                violations = result.get('violations', [])
                
                if violations:
                    for i, violation in enumerate(violations):
                        with st.expander(f"Violation {i+1}: {violation['rule_id']} - {violation['field']}"):
                            st.write(f"**Issue:** {violation['issue']}")
                            if violation.get('sample_data'):
                                st.write("**Sample Violating Data:**")
                                st.write(violation['sample_data'])
                else:
                    st.success("No violations detected!")
            
            with tab3:
                st.header("Remediation Actions")
                remediation_actions = result.get('remediation_actions', [])
                
                if remediation_actions:
                    for i, action in enumerate(remediation_actions):
                        with st.expander(f"Remediation {i+1}: {action['violation']['rule_id']} - {action['violation']['field']}"):
                            st.write(f"**Issue:** {action['violation']['issue']}")
                            st.write("**Remediation Steps:**")
                            st.markdown(action['remediation'])
                else:
                    st.success("No remediation actions needed!")
        else:
            st.error(f"Error: {response.text}")
