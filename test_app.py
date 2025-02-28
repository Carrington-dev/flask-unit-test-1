import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_home(client):
    response = client.get('/')
    assert response.status_code == 200
    assert response.get_json() == {'message': 'Welcome to the Flask App'}

def test_add_numbers(client):
    response = client.get('/add?num1=5&num2=10')
    assert response.status_code == 200
    assert response.get_json() == {'result': 15.0}

def test_add_numbers_invalid(client):
    response = client.get('/add?num1=abc&num2=10')
    assert response.status_code == 400
    assert response.get_json() == {'error': 'Invalid input'}

def test_multiply_numbers_invalid(client):
    response = client.get('/multiply?num1=abc&num2=10')
    assert response.status_code == 400
    assert response.get_json() == {'error': 'Invalid input'}

def test_subtract_numbers_invalid(client):
    response = client.get('/subtract?num1=abc&num2=10')
    assert response.status_code == 400
    assert response.get_json() == {'error': 'Invalid input'}
