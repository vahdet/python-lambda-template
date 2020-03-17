""" Lambda function module """
import os
import json
import boto3

def lambda_handler(event, context):
    """ Handles function event and context """

    # resolve backend api key from the secrets manager
    sm_client = boto3.client('secretsmanager')
    sm_resp = sm_client.get_secret_value(os.getenv('BACKEND_SERVICE_API_KEY_SECRET_ARN'))
    backend_api_key = json.dumps(sm_resp.get('SecretString')).get('key')

    # TODO implement further business logic
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
