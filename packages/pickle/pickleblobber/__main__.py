import os
import pickle
import io
import boto3
import inflect


def process_and_upload_text_chunk(text, folder_name, file_index):

    access_key = os.getenv('PICKLEJAR_ACCESS')
    secret_key = os.getenv('PICKLEJAR_SECRET')
    
    # Initialize the cloud storage session and client
    session = boto3.session.Session()
    client = session.client('s3',
                            region_name='nyc3',
                            endpoint_url='https://nyc3.digitaloceanspaces.com',
                            aws_access_key_id=access_key,
                            aws_secret_access_key=secret_key)
    bucket_name = 'picklejar'  # Your actual bucket name
    
    # Initialize the inflect engine for singularizing words
    engine = inflect.engine()

    # Process the text
    processed_text = ' '.join([engine.singular_noun(word) if engine.singular_noun(word) else word for word in text.split()])

    # Serialize the processed text
    pickled_data = pickle.dumps(processed_text)
    

    # Use the provided folder_name and file_index to create a unique object name for storage
    object_name = f'{folder_name}/text_chunk_{file_index}.p'


    # Upload the serialized data
    with io.BytesIO(pickled_data) as f:
        client.upload_fileobj(f, bucket_name, object_name)

    return f"Chunk {file_index} processed and uploaded successfully to {object_name}."

def main(event, context):

    # Extract 'text', 'folder_name', and 'file_index' directly from the event
    text = event.get('text', '')
    folder_name = event.get('folder_name', 'processed_text')  # Ensure this includes datetime from the app
    file_index = event.get('file_index')  # Ensure this is provided by the app
    
    result = process_and_upload_text_chunk(text, folder_name, file_index)
    

    return {
        "statusCode": 200,
        "body": result
    }
