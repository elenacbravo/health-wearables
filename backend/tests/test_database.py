import pytest
from app import app, db
from models import HealthWearable

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
        yield client
        with app.app_context():
            db.drop_all()

def test_register_wearable(client):
    response = client.post('/wearables', json={'type': 'heart_rate_monitor', 'status': 'active'})
    assert response.status_code == 201
