import pytest
from server import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_hello_route(client):
    """Test the / route"""
    response = client.get('/')
    assert response.status_code == 200
    assert response.json == {"message": "Hello, World!"}

