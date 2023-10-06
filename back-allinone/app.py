from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:Emmanuel_7@localhost/Allinone_db'
db = SQLAlchemy()

# Lancement du Débogueur
app.config["DEBUG"] = True

from model.project import Project, Comments, ProjectTeam, Member, ProjectTeamHasMember


@app.route('/', methods = ['Get'])
def hello_world():
    return 'Hello, World!'

##################### Clients ############################
# Ajouter un nouveau client
@app.route('/admin/client', methods=['POST'])
def create_client()
# Modifier les informations d'un client
# Archiver un client
##################### Projets ############################
@app.route('/admin/project', methods=['POST'])
def create_project():
    data = request.get_json()
    
    new_project = Project(project_name=data['project_name'], project_description=data['project_description'], expired_at=data['expired_at'])
    
    db.session.add(new_project)
    db.session.commit()
    
    return jsonify({'message': 'Project created successfully'}), 201

# Route pour modifier un projet, son status et son commentaire
@app.route('/admin/cp/<int:idproject>', methods=['PUT'])
def update_project(idproject):
    data = request.get_json()
    
    project = Project.query.get(idproject)
    
    if project is None:
        return jsonify({'message': "Projet inexistant"}), 404
    
    if '_idproject_team' in data:
        project._idproject_team = data['_idproject_team']
    if 'project_name' in data:
        project.project_name = data['name']
    if 'project_description' in data:
        project.project_description = data['project_description']
    if 'project_step' in data:
        project.project_step = data['project_step']
    if 'expired_at' in data:
        project.expired_at = data['expired_at']
    if 'Requirement' in data:
        project.Requirement = data['Requirement']
    if 'comments' in data:
        project.comments[0].comments_lib =data['comments']
    if 'status_idstatus' in data:
        project.status_idstatus = data['status_idstatus']
    db.session.commit()
    
    return jsonify({'message': 'Mise a jour effectue'}), 200

@app.route('/admin/cp/<int:idproject>/del', methods=['DELETE'])
def delete_project(idproject):
    project = Project.query.get(idproject)
    db.session.delete(project)
    db.session.commit()
    return jsonify({'message': 'Projet supprime avec succes'}), 200

@app.route('/admin/projects', methods=['GET'])
def list_project():
    projects = db.session.query(Project).all()
    project_list = [{'idproject': project.idproject, 'name': project.project_name, 'description': project.project_description, 'expired_at': project.expired_at, 'created_at': project.created_at, 'status': project.status, 'requirement': project.Requirement} for project in projects]
    return jsonify(projects=project_list)
    

##################### Tasks ############################
# Qjouter une tache
# Modifier une tache
# Suprimer une tache

##################### Equipe ############################
# Creer une nouvelle equipe
@app.route('/admin/team', methods=['POST'])
def create_team():
    data = request.get_json()
    
    new_team = ProjectTeam(team_name=data['team_name'], team_description=['team_description'], )
    db.session.add(new_team)
    db.session.commit()
    return jsonify({'message': 'Team created successfully'}), 201

# Retirer un membre d'une equipe
@app.route('/admin/team/<int:idteam>/delete', methods=['DELETE'])
def delete_member_to_team(idteam):
    try:
        team = ProjectTeam.query.get(idteam)
        if not team:
            return jsonify({'message': 'L\'équipe n\'existe pas'}), 404
        
        # Récupérez les données du membre à ajouter depuis la requête POST
        data = request.get_json()
        username = data['username'] 

        if not username:
            return jsonify({'message': 'L\'username du membre est requis'}), 400
        # Recherche du membre par son nom
        member = Member.query.filter_by(username=username).first()
        
        if not member:
            return jsonify({'message': 'Le membre n\'existe pas'}), 404

        team_member_relation = ProjectTeamHasMember.query.filter_by(
            project_team_idproject_team=team.idproject_team,
            member_idmember=member.idmember
        ).first()
        db.session.delete(team_member_relation)
        db.session.commit()
        
        return jsonify({'message': 'Membre retire de l\'équipe avec succès'}), 201

    except Exception as e:
        # Gérez les erreurs appropriées ici
        return jsonify({'message': 'Une erreur est survenue lors de la supression du membre à l\'équipe'}), 500

# Ajouter un membre a une equipe
@app.route('/admin/team/<int:idteam>', methods=['POST'])
def add_members_to_team(idteam):
    try:
        # Recherche de l'équipe par ID
        team = ProjectTeam.query.get(idteam)
    
        if not team:
            return jsonify({'message': 'L\'équipe n\'existe pas'}), 404

        # Récupérez les données du membre à ajouter depuis la requête POST
        data = request.get_json()
        username = data.get('username') 

        if not username:
            return jsonify({'message': 'L\'ID du membre est requis'}), 400

        # Recherche du membre par son nom
        member = Member.query.filter_by(username=username).first()
        
        if not member:
            return jsonify({'message': 'Le membre n\'existe pas'}), 404

        # Créez une relation entre l'équipe et le membre
        team_member_relation = ProjectTeamHasMember(
            project_team_idproject_team=team.idproject_team,
            member_idmember=member.idmember
        )

        # Ajoutez la relation à la base de données
        db.session.add(team_member_relation)
        db.session.commit()

        return jsonify({'message': 'Membre ajouté à l\'équipe avec succès'}), 201

    except Exception as e:
        # Gérez les erreurs appropriées ici
        return jsonify({'message': 'Une erreur est survenue lors de l\'ajout du membre à l\'équipe'}), 500

# Liste des projets d'une equipe
@app.route('/admin/team/<int:idteam>/lp', methods=['GET'])
def get_team_projects(idteam):
    try:
        projects = Project.query.filter(Project._idproject_team == idteam).all()
        project_list = [{'id': project.idproject, 'name': project.project_name, 'description': project.project_description} for project in projects]

        return jsonify(projects=project_list), 200
    except Exception as e:
        return jsonify({'message': 'Une erreur est survenue lors de la recuperation des liste de l\'équipe'}), 500

##################### Stats ############################

##################### Autre ############################

if __name__ == '__main__':
    db.init_app(app)
    app.run()
