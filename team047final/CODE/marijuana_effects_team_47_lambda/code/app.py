import json
import sklearn
import joblib
import boto3
import os

s3 = boto3.resource('s3')
models = {}

def download_file(filename):
    print(f'downloading {filename}...')
    filepath = f'/tmp/{filename}'
    s3.meta.client.download_file(os.getenv('s3Bucket'), filename, filepath)
    return filepath

def get_prediction(params):
    model_type = params['type']
    input_data = params['input']
    if model_type not in models:
        print(f'loading model for type {model_type} ...')
        filepath = download_file(os.getenv(model_type))
        models[model_type] = joblib.load(open(filepath, 'rb'))
    # example input_data: [11, 1, 991, 1, 1, 1, 1, 1, 2]
    result = models[model_type].predict([input_data])[0]
    return result

def lambda_handler(event, context):
    params = event['queryStringParameters']
    print('params:')
    print(params)
    params['input'] = json.loads(params['input'])
    return {
        'headers': {
            'Access-Control-Allow-Origin': '*'
        },
        'statusCode': 200,
        'body': json.dumps({
            'output': f'{get_prediction(params)}'
        }),
    }
