
from moto import mock_dynamodb2
import boto3
import os 

mock_create_hang = {
            "name": "Crimps",
        }

mock_hang = {
            'id': '1',
            "name": "new hang name"
        }

another_mock_hang = {
            'id': '2',
            "name": "new hang name"
        }
  

@mock_dynamodb2
def setup_mocks():
    dynamodb = boto3.resource('dynamodb')

    table = dynamodb.create_table(
        TableName= os.environ['TABLE_NAME'],
        KeySchema=[
            {
                'AttributeName': 'id',
                'KeyType': 'HASH'  # primary key
            }
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'id',
                'AttributeType': 'S'
            },
        ],
    )
    
    table.put_item(
        Item=mock_hang
    )

    table.put_item(
        Item=another_mock_hang
    )