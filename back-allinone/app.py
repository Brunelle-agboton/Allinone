from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS, cross_origin



app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "http://localhost:8080"}})

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:Emmanuel_7@localhost/db_allinone'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
db = SQLAlchemy()

# Lancement du Débogueur
app.config["DEBUG"] = True

from model.project import *


@app.route('/', methods = ['Get'])
def hello_world():
    return 'Hello, World!'
#*****************************************************************Vue Admin******************************************#
##################### Clients ############################
# Ajouter un nouveau client
@app.route('/admin/client', methods=['POST'])
def create_client():
    data = request.get_json() 
    
    if 'street' in data and 'city' in data and 'postal_code' in data and 'country' in data:
        new_address = ClientAddress(client_street=data['street'], client_city=data['city'], client_postal_code=data['postal_code'], client_state=data['country'])
        db.session.add(new_address)
    else:
        return jsonify({'message': 'Missing address client data'}), 400  # Bad Request

    client_role = Role.query.filter_by(client=1).first()

    if 'client_name' in data and 'client_email' in data and 'client_activity' in data and 'client_tel' in data:
        new_client = ClientUser(client_user_name=data['client_name'], 
                                client_email=data['client_email'], 
                                client_user_activity=data['client_activity'],
                                client_user_no=data['client_tel'],
                                _idclient_address=new_address.idclient_address, 
                                _idrole=client_role.idrole)
        db.session.add(new_client)
        db.session.commit()
        return jsonify({'message': 'Client created successfully'}), 201
    else:
        return jsonify({'message': 'Missing client data'}), 400
# Modifier les informations d'un client
# Archiver un client

# Supprimer un client
@app.route('/admin/client/<int:idclient>', methods=['DELETE'])
def delete_client(idclient):
    client = ClientUser.query.get(idclient)

    if client is None:
        return jsonify({'message': 'Client not found'}), 404

    db.session.delete(client)
    db.session.commit()

    return jsonify({'message': 'Client deleted successfully'}), 200

# Liste des clients
@app.route('/admin/clients', methods=['GET'])
def list_client():
    clients = db.session.query(ClientUser).all()
    if clients:
        client_list = [{'idproject': client.idclient_user, 'name': client.client_user_name, 'client_email': client.client_email, 'activity': client.client_user_activity, 'tel': client.client_user_no} for client in clients]
    else:
        client_list = []
    return jsonify(client_list)
  
##################### Projets ############################
@app.route('/admin/project', methods=['POST'])
def create_project():
    data = request.get_json()
    
    new_project = Project(project_name=data['project_name'], project_description=data['project_description'], expired_at=data['expired_at'])
    
    db.session.add(new_project)
    db.session.commit()
    
    return jsonify({'message': 'Project created successfully', 'idproject': new_project.idproject}), 201

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

# Liste des projeta
@app.route('/admin/projects', methods=['GET'])
def list_project():
    projects = db.session.query(Project).all()
    project_list = []
    if projects:
        for project in projects:
                comment = Comments.query.filter_by(project_idproject=project.idproject)
                project_data = {'idproject': project.idproject, 
                                'name': project.project_name, 
                                'description': project.project_description, 
                                'expired_at': project.expired_at, 
                                'created_at': project.created_at, 
                                'status': project.project_status, 
                                'requirement': project.requirement, 
                                'progress': project.project_step,
                                'comments': [comments.comment_text for comments in comment]}  # Ajoutez ici les données des commentaires
                project_list.append(project_data)
    else:
        project_list = []
    return jsonify(project_list)
    
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

#*****************************************************************************Vue Equipe Projet********************************************************#

##################### Tasks ############################
# Ajouter une tache
@app.route('/project/<int:idproject>/tasks', methods=['POST'])
def create_task(idproject):
    data = request.get_json()
    new_task = Tasks(
        tasks_description=data['description'],
        added_at=data['added_at'],
        finished_at=data['finished_at'],
        project_idproject=idproject
    )
    db.session.add(new_task)
    db.session.commit()
    return jsonify({'message': 'Task created successfully'}), 201

# Modifier une tache
@app.route('/project/<int:idproject>/tasks/<int:idtasks>', methods=['PUT'])
def update_task(idproject, idtasks):
    data = request.get_json()
    task = Tasks.query.filter_by(idtasks=idtasks, project_idproject=idproject).first()

    if task is None:
        return jsonify({'message': 'Task not found'}), 404

    if 'description' in data:
        task.tasks_description = data['description']
    if 'updated_at' in data:
        task.added_at = data['updated_at']
    if 'finished_at' in data:
        task.finished_at = data['finished_at']
    if 'status' in data:
        task.status_idstatus=data['status'],

    db.session.commit()
    return jsonify({'message': 'Task updated successfully'}), 200

# Suprimer une tache
@app.route('/project/<int:idproject>/tasks/<int:idtasks>', methods=['DELETE'])
def delete_task(idproject, idtasks):
    task = Tasks.query.filter_by(idtasks=idtasks, project_idproject=idproject).first()

    if task is None:
        return jsonify({'message': 'Task not found'}), 404

    db.session.delete(task)
    db.session.commit()
    return jsonify({'message': 'Task deleted successfully'}), 200

# Assiggner une tache a un membre
@app.route('/project/<int:idproject>/tasks/<int:idtasks>/assign-member', methods=['POST'])
def assign_task_to_members(idtasks):
    task = Tasks.query.get(idtasks)
    if not task:
        return jsonify({'message': 'Tâche non trouvée'}), 404

    member_names = request.get_json().get('members', [])  # Changez 'username' en 'members' pour correspondre à votre JSON
    members = Member.query.filter(Member.username.in_(member_names)).all()

    if not members:
        return jsonify({'message': 'Aucun membre trouvé'}), 404

    # Créer une relation entre une tâche et un membre, ajouter cette relation à la base de données
    for member in members:
        task_member_relation = MemberHasTasks(
            member_idmember=member.idmember,
            tasks_idtasks=idtasks,
            tasks_project_idproject=task.project_idproject,
            tasks_project_project_team_idproject_team=task.project_project_team_idproject_team  
        )
        db.session.add(task_member_relation)

    db.session.commit()

    return jsonify({'message': 'Tâche assignée aux membres avec succès'}),

#Modifier un membre d'une tache
@app.route('/project/<int:idproject>/tasks/<int:idtasks>/assign-member', methods=['PUT'])
def change_task_member(idproject, idtasks):
    task = Tasks.query.get(idtasks)
    if not task:
        return jsonify({'message': 'Tâche non trouvée'}), 404

    data = request.get_json()
    new_member_name = data.get('new_member', None)

    if not new_member_name:
        return jsonify({'message': 'Nom du nouveau membre non fourni'}), 400

    # Rechercher le membre existant avec le nouveau nom
    new_member = Member.query.filter_by(username=new_member_name).first()

    if not new_member:
        return jsonify({'message': 'Nouveau membre non trouvé'}), 404

    # Mettre à jour le membre de la tâche
    task_member_relation = MemberHasTasks.query.filter_by(
        tasks_idtasks=idtasks, tasks_project_idproject=task.project_idproject,
        tasks_project_project_team_idproject_team=task.project_project_team_idproject_team
    ).first()

    if not task_member_relation:
        return jsonify({'message': 'Relation membre-tâche non trouvée'}), 404

    task_member_relation.member_idmember = new_member.idmember
    db.session.commit()

    return jsonify({'message': 'Membre de la tâche modifié avec succès'}), 200

#Supprimer un membre d'une tache
@app.route('/project/<int:idproject>/tasks/<int:idtasks>/members/<int:idmember>', methods=['DELETE'])
def remove_task_member(idproject, idtasks, idmember):
    task = Tasks.query.get(idtasks)
    if not task:
        return jsonify({'message': 'Tâche non trouvée'}), 404

    # Vérifier si la relation membre-tâche existe
    task_member_relation = MemberHasTasks.query.filter_by(
        tasks_idtasks=idtasks, tasks_project_idproject=task.project_idproject,
        tasks_project_project_team_idproject_team=task.project_project_team_idproject_team,
        member_idmember=idmember
    ).first()

    if not task_member_relation:
        return jsonify({'message': 'Relation membre-tâche non trouvée'}), 404

    # Supprimer la relation membre-tâche de la base de données
    db.session.delete(task_member_relation)
    db.session.commit()

    return jsonify({'message': 'Membre de la tâche supprimé avec succès'}), 200

#Ajouter un domain a un membre
@app.route('/assign-member-to-domain/<int:member_id>/<int:domain_id>', methods=['POST'])
def assign_member_to_domain(member_id, domain_id):
    member = Member.query.get(member_id)
    if not member:
        return jsonify({'message': 'Membre non trouvé'}), 404

    domain = Domain.query.get(domain_id)
    if not domain:
        return jsonify({'message': 'Domaine non trouvé'}), 404

    domain.members.append(member)
    db.session.commit()

    return jsonify({'message': 'Membre assigné au domaine avec succès'}), 200


if __name__ == '__main__':
    db.init_app(app)
    app.run()
