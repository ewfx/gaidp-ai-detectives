# lambda_function.py
import json
import boto3
import pandas as pd
import os
import tempfile

# This Lambda function handles API Gateway requests, retrieves files from S3, 
# processes them using our regulatory data profiling functions, and returns the results.

# Import the main processing functions
from core_processing  import process_regulatory_data_profiling

def lambda_handler(event, context):
    try:
        # Parse the event
        body = json.loads(event['body']) if 'body' in event else event
        
        # Get the instruction file and transaction data from S3
        instructions_file = body.get('instructions_file')
        transaction_file = body.get('transaction_file')
        
        if not instructions_file or not transaction_file:
            return {
                'statusCode': 400,
                'body': json.dumps({'error': 'Both instructions_file and transaction_file are required'})
            }
        
        # Get files from S3
        s3_client = boto3.client('s3')
        bucket_name = os.environ.get('S3_BUCKET_NAME', 'genaidetectives')
        
        # Download files from S3 to temporary directory
        with tempfile.NamedTemporaryFile(delete=False, suffix='.csv') as temp_instructions:
            s3_client.download_file(bucket_name, instructions_file, temp_instructions.name)
            instructions_path = temp_instructions.name
        
        with tempfile.NamedTemporaryFile(delete=False, suffix='.csv') as temp_transactions:
            s3_client.download_file(bucket_name, transaction_file, temp_transactions.name)
            transactions_path = temp_transactions.name
        
        # Process the data
        result = process_regulatory_data_profiling(instructions_path, transactions_path)
        
        # Clean up temporary files
        os.unlink(instructions_path)
        os.unlink(transactions_path)
        
        # Return the results
        return {
            'statusCode': 200,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            },
            'body': json.dumps(result, default=str)
        }
    
    except Exception as e:
        import traceback
        return {
            'statusCode': 500,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            },
            'body': json.dumps({
                'error': str(e),
                'traceback': traceback.format_exc()
            })
        }
