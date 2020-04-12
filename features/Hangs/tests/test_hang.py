
from features.Hangs.hang import resolve_hang, resolve_hangs, create_hang, update_hang
from aws_resources.mock_dynamo import setup_mocks, mock_hang, another_mock_hang, mock_create_hang
from moto import mock_dynamodb2

@mock_dynamodb2
def test_resolve_hang():
    setup_mocks()
    hang = resolve_hang({}, {}, "1")
    assert hang == mock_hang
    
@mock_dynamodb2
def test_resolve_hang():
    setup_mocks()
    hangs = list(resolve_hangs({'hangs': ["1", "2"]}, {}))
    assert hangs == [mock_hang, another_mock_hang]

@mock_dynamodb2
def test_create_hang():
    setup_mocks()
    response = create_hang({}, {}, mock_create_hang)
    assert response['message'] == 'success' and response['hang']['name'] == 'Crimps'

@mock_dynamodb2
def test_update_hang():
    setup_mocks()
    new_attr = {'title': 'new hang name'}
    updated_hang = {**mock_hang, **new_attr}
    response = update_hang({}, {}, updated_hang)
    assert response['message'] == 'success' and response['hang']['name'] == 'new hang name'