import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_home_endpoint(client):
    """Garante que a rota raiz está online e responde status 200"""
    response = client.get('/')
    assert response.status_code == 200
    assert b"online" in response.data