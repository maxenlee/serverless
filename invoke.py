import boto3

lambda_client = boto3.client('lambda')

def invoke_process_function_async(payload):
    response = lambda_client.invoke(
        FunctionName='process_and_upload_text_chunk',
        InvocationType='Event',  # This specifies asynchronous execution
        Payload=json.dumps(payload),
    )
    return response
