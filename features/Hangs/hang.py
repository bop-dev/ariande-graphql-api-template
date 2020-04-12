from aws_resources.dynamo import build_update_expression, build_update_attributes_dictionary, table
from boto3.dynamodb.conditions import Key
import uuid

def resolve_hang(obj, info, id):
    hang = table().query(
        KeyConditionExpression=Key('id').eq(id)
    )['Items'][0]
    return hang

def resolve_hangs(obj, info):
    ids = obj['hangs']
    return map(lambda id: resolve_hang(obj, info, id), ids)

def create_hang(obj, info, hang):
    id = str(uuid.uuid4())
    hang['id'] = id
    table().put_item(Item=hang)
    return {
        'hang': hang,
        'message': 'success',
        'code': 200,
        'success': True
    }

def update_hang(obj, info, hang):
    attributes_to_update = build_update_attributes_dictionary(hang)
    update_expression = build_update_expression(hang)
    table().update_item(
        Key={
            'id': hang['id']
        },
        UpdateExpression=update_expression,
        ExpressionAttributeValues=attributes_to_update,
    )
    updated_hang = table().query(
        KeyConditionExpression=Key('id').eq(hang['id'])
    )['Items'][0]

    return {
        'hang': updated_hang,
        'message': 'success',
        'code': 200,
        'success': True
    }