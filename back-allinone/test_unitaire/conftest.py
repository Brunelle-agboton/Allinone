import pytest
from app import app, db

# Configuration des tests
@pytest.fixture
def client(scope='session'):
    app.config['TESTING'] = True

    # Create a testing client
    client = app.test_client()

    with app.app_context():
        # Initialize the database
        db.create_all()
        yield client
        db.drop_all()
