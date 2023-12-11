import os
import pytest
from app import app, db

# Utilisez un client pytest-flask pour les tests
@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    client = app.test_client()

    with app.app_context():
        db.create_all()

    yield client

# Test de base pour s'assurer que l'application s'exécute correctement
def test_hello_world(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'Hello, World!' in response.data

# Test de l'API /admin/team/<int:idteam>
def test_get_team(client):
    # Créez des données de test dans la base de données
    with app.app_context():
        # Ajoutez ici des données de test à la base de données, si nécessaire
        pass

    # Appelez l'API /admin/team/<int:idteam>
    response = client.get('/admin/team/1')
    assert response.status_code == 200

    # Vérifiez le contenu de la réponse
    data = response.get_json()
    assert 'idproject_team' in data
    assert 'team_name' in data
    assert 'team_description' in data
    assert 'created_at' in data
    assert 'updated_at' in data
    assert 'nb_projet' in data
    assert 'projets' in data
    assert 'members' in data

# Ajoutez d'autres tests au besoin

# Nettoyez la base de données après les tests
def pytest_sessionfinish(session, exitstatus):
    with app.app_context():
        db.drop_all()
