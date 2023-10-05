from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:Emmanuel_7@localhost/Allinone_db'
db = SQLAlchemy()

# Lancement du Débogueur
app.config["DEBUG"] = True

from model.project import Project


@app.route('/', methods = ['Get'])
def hello_world():
    return 'Hello, World!'

##################### Clients ############################

##################### Projets ############################
@app.route('/admin/project', methods=['POST'])
def create_project():
    data = request.get_json()
    
    new_project = Project(name=data['name'], description=data['description'])
    db.session.add(new_project)
    db.session.commit()
    return jsonify({'message': 'Project created successfully'}), 201

@app.route('/admin/cp', methods=['PUT'])
def update_project():
    data = request.get_json()

@app.route('/admin/projects', methods=['Get'])
def list_project():
    projects = db.session.query(Project).all()
    project_list = [{'id': project.idproject, 'name': project.project_name, 'description': project.project_description, 'expired_at': project.expired_at, 'created_at': project.created_at, 'status': project.status, 'requirement': project.Requirement} for project in projects]
    return jsonify(projects=project_list)
    
##################### Stats ############################

##################### Autre ############################

if __name__ == '__main__':
    db.init_app(app)
    app.run()
