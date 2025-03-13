import pytest
import sys
import os

# Add project root directory to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app import app

@pytest.fixture
def client():
    app.testing = True
    return app.test_client()

def test_home(client):
    """Test if the home page returns 'Hello moto!'"""
    response = client.get('/')
    assert response.status_code == 200
    assert response.data.decode() == "Hello Deveops!"
