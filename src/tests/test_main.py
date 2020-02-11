import pytest

from src.routes.v1 import v1

def test_health(client):
    response = client.get(v1.path + '/health')
    assert response.status_code == 200
    assert response.json() == {}


def test_get_users_unauthorized(client):
    response = client.get(v1.path + '/users')

    payload = {
        'code': 403,
        'error': 'Forbidden',
    }

    assert response.status_code == 403
    assert response.json() == payload


def test_register_no_payload(client):
    response = client.post(v1.path + '/register')

    assert response.status_code == 400

required_fields = {
    'email': 'test@gmail.com',
    'username': 'test_user',
    'password': 'test_password',
}

bad_payloads = [(required_fields) for x in required_fields.keys()]

@pytest.mark.parametrize('json', bad_payloads)
def test_register_bad_payload(client, json):
    print(json)
    #response = client.post(v1.path + '/register', json=json)

    #assert response.status_code == 400
