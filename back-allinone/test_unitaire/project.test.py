import pytest
from app import app, db

@pytest.fixture
def testing():
    app.config['TESTING'] = True
    with app.app_context():
        yield testing
