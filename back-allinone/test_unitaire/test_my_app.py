import pytest
from app import app, db  # Import your Flask app instance and SQLAlchemy db
from model.project import Role
from test_unitaire.conftest import client
from flask import session

# Test to create a client
def test_create_client(client):
    # Ensure Flask-SQLAlchemy knows about the app
    with app.app_context():
        # You can use the client to send a simulated POST request to create a client
        client_role = Role.query.filter_by(client=1).first()

        response = client.post('/admin/client', json={
            'client_street': '123 Main St',
            'client_city': 'nabonne',
            'client_postal_code': '50000',
            'client_state': 'Pays bas',
            'client_user_name': 'Nom du client',
            'client_email': 'client@email.com',
            'client_user_activity': 'Activité du client',
            'client_user_no': '1234567890',
            '_idrole': client_role.idrole
        })
        
        assert response.status_code == 201  # Ensure client creation returns a 201 status code
