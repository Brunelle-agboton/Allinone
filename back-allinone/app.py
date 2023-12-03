import os
from flask import Flask, request, jsonify
from flask_bcrypt import Bcrypt
from dotenv import load_dotenv

from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS, cross_origin

app = Flask(__name__)

CORS(app, methods=['POST', 'GET', 'PUT', 'DELETE', 'OPTIONS'], resources={r"/*": {"origins": "http://localhost:8080", "supports_credentials": True}})

bcrypt = Bcrypt(app)
load_dotenv()

# Configurer la base de données SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = os.getenv('SQLALCHEMY_TRACK_MODIFICATIONS')

db = SQLAlchemy()

# Configurer l'environnement de développement
app.config['FLASK_ENV'] = os.getenv('FLASK_ENV')
app.config['FLASK_DEBUG'] = os.getenv('FLASK_DEBUG')

from model.project import *


@app.route('/', methods = ['Get'])
def hello_world():
    return 'Hello, World!'

@app.after_request
def after_request(response):
  response.headers['Access-Control-Allow-Methods']='*'
  response.headers['Access-Control-Allow-Origin']='*'
  response.headers['Vary']='Origin'
  return response
#*****************************************************************Vue Admin******************************************
##################### Gestion des membres ############################
@app.route('/admin/mem', methods=['POST'])
def add_member():
    data = request.get_json()

    if 'username' not in data or 'password' not in data or 'email' not in data:
        return jsonify({'message': 'Le nom d\'utilisateur et le mot de passe sont requis'}), 400

    new_member = Member(username=data['username'], email=data.get('email'))
    new_member.set_password(data['password'])

    
    try:
        db.session.add(new_member)
        db.session.commit()
        return jsonify({'message': 'Membre créé avec succès'}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'message': f'Erreur lors de la création du membre: {str(e)}'}), 500

@app.route('/admin/members', methods=['GET'])
def get_members():
    members = Member.query.all()
    output = []
    for member in members:
        member_data = {'idmember': member.idmember,'username': member.username}
        output.append(member_data)
    return jsonify(output)
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
        client_list = [{'idproject': client.idclient_user, 
                        'name': client.client_user_name, 
                        'client_email': client.client_email, 
                        'activity': client.client_user_activity, 
                        'tel': client.client_user_no} for client in clients]
    else:
        client_list = []
    return jsonify(client_list)
  
##################### Projets ############################
@app.route('/admin/project', methods=['POST'])
def create_project():
    """
    Create a new project.

    This route allows the creation of a new project by accepting a JSON payload
    containing the project details. The required fields in the JSON payload are:
    - project_name: The name of the project.
    - project_description: The description of the project.
    - expired_at: The expiration date of the project.

    Method: POST
    Request Payload:
    {
        "project_name": "Example Project",
        "project_description": "Description of the project.",
        "expired_at": "2023-12-31"  # Format: YYYY-MM-DD
    }

    Returns:
    - If successful, returns a JSON response with a success message and the
      ID of the created project.
        {
            "message": "Project created successfully",
            "idproject": 1  # ID of the created project
        }
    - If there is an error or missing data, returns an appropriate error message.

    HTTP Status Codes:
    - 201 Created: Project created successfully.
    - 400 Bad Request: Invalid or missing data in the request payload.
    """
    data = request.get_json()
    
    new_project = Project(project_name=data['project_name'], 
                          project_description=data['project_description'], 
                          expired_at=data['expired_at'])
    db.session.add(new_project)
    db.session.commit()
    
    return jsonify({'message': 'Project created successfully', 'idproject': new_project.idproject}), 201

#Route pour recuperer un projet avec son id
@app.route('/admin/project/<int:idproject>')
def get_project(idproject):
    # Recuperer le projet correspondant à l'ID
    project = db.session.get(Project, idproject)

    if project is not None:
         # Accédez aux relations et récupérez les données associées
        comments = [comment.comments_lib for comment in project.comments]
        # tasks = [task.task_name for task in project.tasks]
        # resumes = [resume.resume_content for resume in project.resumes]
        if project.project_team:
            team_data = {
                'idproject_team': project.project_team.idproject_team,
                'team_name': project.project_team.team_name,
                'team_description': project.project_team.team_description,
                'created_at': project.project_team.created_at.strftime("%Y-%m-%d"),
                'updated_at': project.project_team.updated_at.strftime("%Y-%m-%d")
                # Ajoutez d'autres champs si nécessaire
            }
        else:
            team_data = None
        #if team:
        #    team_members = team.members
        #    team_members_all = [member.name for member in team_members]
        #    team_members_all.append(team_members.idproject_team)
        #else:
        #    team_members_all = []
        
        created_date = project.created_at.strftime("%Y-%m-%d")
        expired_date = project.expired_at.strftime("%Y-%m-%d")
        
        project_data = {'idproject': project.idproject, 
                        'project_name': project.project_name, 
                        'description': project.project_description, 
                        'expired_at': expired_date, 
                        'created_at': created_date, 
                        'status': project.project_status, 
                        'requirement': project.requirement, 
                        'progress': project.project_step,
                        'comments': comments,
                        'team': team_data
                        }  
        return jsonify(project_data)
    else:
        return jsonify({"error": "Projet non trouvé"}), 404
    
# Route pour modifier un projet, son status et son commentaire
@app.route('/admin/editp/<int:idproject>', methods=['PUT'])
def update_project(idproject):
    data = request.get_json()
    #print(data)
    project = db.session.get(Project, idproject)
    

    if project is None:
        return jsonify({'message': "Projet inexistant"}), 404
        
    if 'team' in data:
        project_team = db.session.query(ProjectTeam).filter_by(team_name=data['team']).first()
        if project_team is not None:
            project.project_team = project_team
    if 'project_name' in data:
        project.project_name = data['project_name']
    if 'project_description' in data:
        project.project_description = data['description']
    if 'progress' in data:
        project.project_step = data['progress']
    if 'expired_at' in data:
        project.expired_at = data['expired_at']
    if 'requirement' in data:
        #setattr(project,requirement,data['requirement'])
        project.requirement = data['requirement']
    if 'comments' in data:
        if project.comments:
            project.comments[0].comments_lib = data['comments']
        else:
            if data['comments']:
                new_comment = Comments(comments_lib=data['comments'],project_idproject=idproject)
                db.session.add(new_comment)
                
            project.comments=data['comments']
    if 'status_idstatus' in data:
        project.status_idstatus = data['status_idstatus']
    
    db.session.add(project)            
    db.session.commit()
    
    return jsonify(project), 200

@app.route('/admin/delp/<int:idproject>', methods=['DELETE'])
def delete_project(idproject):
    project = Project.query.get(idproject)
    db.session.delete(project)
    db.session.commit()
    return jsonify({'message': 'Projet supprime avec succes'}), 200

# Liste des projets
@app.route('/admin/projects', methods=['GET'])
def list_project():    
    projects = Project.query.all()
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
                                'comments': [comments.comment_text for comments in comment]}
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
    return jsonify({'message': 'Team created successfully'}), 200

#Supprimer une equipe
@app.route('/admin/delt/<int:idteam>', methods=['DELETE'])
def delete_team(idteam):
    team = ProjectTeam.query.get(idteam)
    db.session.delete(team)
    db.session.commit()
    return jsonify({'message': 'Team supprime avec succes'}), 200

# Retirer un membre d'une equipe
@app.route('/admin/team/<int:idteam>/del/<int:idmember>', methods=['DELETE'])
@cross_origin()
def delete_member_to_team(idteam, idmember):
    print(request)
    team = db.session.get(ProjectTeam, idteam)
    if not team:
        return jsonify({'message': 'L\'équipe n\'existe pas'}), 404
    
    member = db.session.get(Member, idmember)
        
    if not member:
        return jsonify({'message': 'Le membre n\'existe pas'}), 404

    team_member_relation = ProjectTeamHasMember.query.filter_by(
        project_team_idproject_team=team.idproject_team,
        member_idmember=member.idmember
    ).first()
    db.session.delete(team_member_relation)
    db.session.commit()
    
    return jsonify({'message': 'Membre retire de l\'équipe avec succès'}), 201
    
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

@app.route('/admin/teams', methods=['GET'])
def list_team():
    teams = ProjectTeam.query.all()
    team_list = []
    if teams:
        for team in teams:
            team_dict = {'idteam': team.idproject_team,
                        'name': team.team_name,
                        'description': team.team_description,
                        'created_at': team.created_at,
                        }
            team_list.append(team_dict)
    else:
        team_list = []
    return jsonify(team_list)

# Liste des projets d'une equipe
@app.route('/admin/team/<int:idteam>', methods=['GET'])
def get_team(idteam):
    
    team =  db.session.get(ProjectTeam, idteam)
    if team is not None:
        #Récupérer tous les projets de l'équipe
        projects = Project.query.filter(Project._idproject_team == idteam).all()
        if projects is not None:
            project_list = [{'id': project.idproject, 'name': project.project_name, 'description': project.project_description} for project in projects]
        else:
            project_list = []
        
        #Récupérer tous les membres de l'équipe   
        team_members = team.members
        team_members_all = [{'idmember': member.idmember, 'username': member.username} for member in team_members]
        #Récupérer les champs de l'équipe et ajouter les données précedemment récupérées
        team_data = {
            'idproject_team': team.idproject_team,
            'team_name': team.team_name,
            'team_description': team.team_description,
            'created_at': team.created_at.strftime("%Y-%m-%d"),
            'updated_at': team.updated_at.strftime("%Y-%m-%d"),
            'nb_projet': len(projects),
            'projets': project_list,
            'members': team_members_all,
        }

        return jsonify(team_data), 200
    else:
        return jsonify({'message': 'Une erreur est survenue lors de la recuperation des liste de l\'équipe'}), 500

#Mettre a jour une equipe
@app.route('/admin/editeq/<int:idteam>', methods=['PUT'])
@cross_origin()
def update_team(idteam):
    data = request.get_json()
    print(request)
    # Récupérer les détails de l'équipe depuis la base de données
    team =  db.session.get(ProjectTeam, idteam)
    if team is None:
        return jsonify({'message': "Team inexistant"}), 404
    
    if 'team_name' in data:
        team.team_name = data['team_name']
    if 'team_description' in data:
        team.team_description = data['team_description']
    if 'members' in data:
        members_ids = data['members']
        team.members = [db.session.get(Member, member_id) for member_id in members_ids]

        #for member in members:
    db.session.add(team)            
    db.session.commit()
    
    team_data = {
            'idproject_team': team.idproject_team,
            'team_name': team.team_name,
            'team_description': team.team_description,
            'created_at': team.created_at.strftime("%Y-%m-%d"),
            'updated_at': team.updated_at.strftime("%Y-%m-%d"),
        }
    
    return jsonify(team_data), 200

##################### Stats ############################

##################### Autre ############################
#
"""
Elle récupère les données de la requête et vérifie si username, email et mot de passe sont présents
Puis le nouvequ membre est créé avec le role correspondant
"""
@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()

    if 'username' not in data or 'password' not in data or 'email' not in data:
        return jsonify({'message': 'Le nom d\'utilisateur, le mot de passe et l\'email sont requis'}), 400

    new_member = Member(username=data['username'], email=data.get('email'))
    new_member.set_password(data['password'])

    # Ajouter le rôle utilisateur par défaut
    user_role = Role.query.filter_by(user=True).first()
    new_member.roles.append(user_role)

    try:
        db.session.add(new_member)
        db.session.commit()
        return jsonify({'message': 'Membre créé avec succès'}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'message': f'Erreur lors de la création du membre: {str(e)}'}), 500

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()

    if 'username' not in data or 'password' not in data:
        return jsonify({'message': 'Le nom d\'utilisateur et le mot de passe sont requis'}), 400

    member = Member.query.filter_by(username=data['username']).first()

    if member and member.check_password(data['password']):
        # Vous pouvez inclure ici la logique pour générer le token d'authentification
        return jsonify({'message': 'Connexion réussie'}), 200
    else:
        return jsonify({'message': 'Nom d\'utilisateur ou mot de passe incorrect'}), 401

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
