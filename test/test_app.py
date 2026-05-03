import pytest
from app.main import app

@pytest.fixture
def client():
    # Sets up a virtual browser to test the app without running it
    with app.test_client() as client:
        yield client

def test_home_page(client):
    """Test that the home page returns a 200 status code."""
    response = client.get('/')
    assert response.status_code == 200
    assert b"automated pipeline" in response.data

def test_health_check(client):
    """Test the health check endpoint."""
    response = client.get('/health')
    assert response.status_code == 200
    assert response.json['status'] == "healthy"

# FOR YOUR TASK 1 EXERCISE:
# To intentionally break the test for your recording, 
# uncomment the line below or change 200 to 500.
# def test_intentional_failure():
#     assert 1 == 2