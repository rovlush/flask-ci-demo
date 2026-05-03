import pytest
from app.app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_home(client):
    """Test the home route returns success status."""
    response = client.get('/')
    assert response.status_code == 200
    assert response.get_json()['status'] == 'success'

def test_health(client):
    """Test the health check route."""
    response = client.get('/health')
    assert response.status_code == 200
    assert response.get_json()['status'] == 'healthy'