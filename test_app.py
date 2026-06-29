import pytest
from app import app

def test_home_endpoint():
    """Teste básico funcional para passar no pipeline"""
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 200