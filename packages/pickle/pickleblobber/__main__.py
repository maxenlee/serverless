import os
import pickle
import io
import boto3
import inflect

<<<<<<< HEAD

def process_and_upload_text_chunk(text, folder_name, file_index):

=======
def process_and_upload_text_chunks(chunk, folder_name, file_name):
>>>>>>> 1f3f952 (pickling)
    access_key = os.getenv('PICKLEJAR_ACCESS')
    secret_key = os.getenv('PICKLEJAR_SECRET')

    # Initialize the cloud storage session and client
    session = boto3.session.Session()
    client = session.client('s3',
                            region_name='nyc3',
                            endpoint_url='https://nyc3.digitaloceanspaces.com',
                            aws_access_key_id=access_key,
                            aws_secret_access_key=secret_key)
    bucket_name = 'picklejar'

    # Initialize the inflect engine for singularizing words
    engine = inflect.engine()

    # Process the chunk
    processed_chunks_with_indices = [{
        'index': item['index'],
        'text': ' '.join([engine.singular_noun(word) if engine.singular_noun(word) else word for word in item['text'].split()])
    } for item in chunk]

<<<<<<< HEAD
    # Serialize the processed text
    pickled_data = pickle.dumps(processed_text)
    

    # Use the provided folder_name and file_index to create a unique object name for storage
    object_name = f'{folder_name}/text_chunk_{file_index}.p'
=======
    # Serialize the processed chunks with indices
    pickled_data = pickle.dumps(processed_chunks_with_indices)

    # Construct the object name using folder and file name
    object_name = f'{folder_name}/{file_name}'
>>>>>>> 1f3f952 (pickling)


    # Upload the serialized data
    with io.BytesIO(pickled_data) as f:
        client.upload_fileobj(f, bucket_name, object_name)

    return f"Chunks processed and uploaded successfully to {object_name}."

def main(event, context):
<<<<<<< HEAD

    # Extract 'text', 'folder_name', and 'file_index' directly from the event
    text = event.get('text', '')
    folder_name = event.get('folder_name', 'processed_text')  # Ensure this includes datetime from the app
    file_index = event.get('file_index')  # Ensure this is provided by the app
    
    result = process_and_upload_text_chunk(text, folder_name, file_index)
    
=======
    chunk = event['chunk']
    folder_name = event['folder_name']
    file_name = event['file_name']  # File name specified by the app
    
    result = process_and_upload_text_chunks(chunk, folder_name, file_name)
>>>>>>> 1f3f952 (pickling)

    return {
        "statusCode": 200,
        "body": result
    }
