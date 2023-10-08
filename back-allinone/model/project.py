from app import db
from sqlalchemy.orm import relationship

class Project(db.Model):
    __tablename__ = 'project'
    idproject = db.Column(db.Integer, primary_key=True)
    project_name = db.Column(db.String(45), nullable=False)
    project_description = db.Column(db.String(255))
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    update_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    expired_at = db.Column(db.DateTime)
    status_idstatus = db.Column(db.Integer, db.ForeignKey('status.idstatus'),nullable=False, default=1)
    _idproject_team = db.Column(db.Integer, db.ForeignKey('project_team.idproject_team'), nullable=True)
    project_step = db.Column(db.Text)
    Requirement = db.Column(db.String(255), nullable=True)
    comments = relationship("Comments", back_populates="project")

class ClientUser(db.Model):
    __tablename__ = 'client_user'
    idclient_user = db.Column(db.Integer, primary_key=True)
    client_user_name = db.Column(db.String(45))
    client_email = db.Column(db.String(64))
    client_user_activity = db.Column(db.String(45))
    client_user_no = db.Column(db.String(45))
    _idclient_address = db.Column(db.Integer, db.ForeignKey('client_address.idclient_address'), nullable=False)
    _idrole = db.Column(db.Integer, db.ForeignKey('role.idrole'), nullable=False, default=1)

class ClientAddress(db.Model):
    __tablename__ = 'client_address'
    idclient_address = db.Column(db.Integer, primary_key=True)
    street = db.Column(db.String(55))
    postal_code = db.Column(db.String(10))
    city = db.Column(db.String(15))
    country = db.Column(db.String(25))

class ClientUserHasProject(db.Model):
    __tablename__ = 'client_user_has_project'
    client_user_idclient_user = db.Column(db.Integer, db.ForeignKey('client_user.idclient_user'), primary_key=True)
    project_idproject = db.Column(db.Integer, db.ForeignKey('project.idproject'), primary_key=True)
    project_project_team_idproject_team = db.Column(db.Integer, db.ForeignKey('project_team.idproject_team'), primary_key=True)
    
    client_user = db.relationship('ClientUser', foreign_keys=[client_user_idclient_user])
    project = db.relationship('Project', foreign_keys=[project_idproject])
    project_team = db.relationship('ProjectTeam', foreign_keys=[project_project_team_idproject_team])

class Comments(db.Model):
    __tablename__ = 'comments'
    idcomments = db.Column(db.Integer, primary_key=True)
    comments_lib = db.Column(db.Text)
    _idproject = db.Column(db.Integer, db.ForeignKey('project.idproject'))
    _idproject_team = db.Column(db.Integer, db.ForeignKey('project_team.idproject_team'))
    updated_at = db.Column(db.DateTime, server_default=db.func.current_timestamp())
    
    project = db.relationship('Project', foreign_keys=[_idproject])
    project_team = db.relationship('ProjectTeam', foreign_keys=[_idproject_team])
    project = relationship("Project", back_populates="comments")
    
class Status(db.Model):
    __tablename__ = "status"
    idstatus = db.Column(db.Integer, primary_key=True)
    status_name = db.Column(db.String(15), nullable=False)
    
class ProjectTeam(db.Model):
    __tablename__ = 'project_team'
    idproject_team = db.Column(db.Integer, primary_key=True)
    team_name = db.Column(db.String(45))
    team_description = db.Column(db.String(64))
    created_at = db.Column(db.DateTime,default=db.func.current_timestamp())
    last_modified = db.Column(db.DateTime, default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp())
    
class Member(db.Model):
    __tablename__ = 'member'
    idmember = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(45), nullable=False)
    email = db.Column(db.String(255))
    password = db.Column(db.String(32), nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    role_idrole1 = db.Column(db.Integer, db.ForeignKey('role.idrole'), nullable=False)

class ProjectTeamHasMember(db.Model):
    __tablename__ = 'project_team_has_member'
    project_team_idproject_team = db.Column(db.Integer, db.ForeignKey('project_team.idproject_team'), primary_key=True)
    member_idmember = db.Column(db.Integer, db.ForeignKey('member.idmember'), primary_key=True)

class Role(db.Model):
    __tablename__ = 'role'
    idrole = db.Column(db.Integer, primary_key=True)
    super_admin = db.Column(db.Boolean)
    admin = db.Column(db.Boolean)
    user = db.Column(db.Boolean)
    client = db.Column(db.Boolean)

class Tasks(db.Model):
    __tablename__ = 'tasks'
    idtasks = db.Column(db.Integer, primary_key=True)
    tasks_description = db.Column(db.String(255), nullable=False)
    added_at = db.Column(db.Date, nullable=False)
    finished_at = db.Column(db.Date, nullable=False)
    tasks_status = db.Column(db.String(45), nullable=False)
    project_idproject = db.Column(db.Integer, db.ForeignKey('project.idproject'), nullable=False)
    status_idstatus = db.Column(db.Integer, db.ForeignKey('status.idstatus'), nullable=False, default=1)
    status = db.relationship('Status', backref='tasks')
    project_project_team_idproject_team = db.Column(db.Integer, db.ForeignKey('project_team.idproject_team'), nullable=False)

class MemberHasTasks(db.Model):
    __tablename__ = 'member_has_tasks'
    member_idmember = db.Column(db.Integer, db.ForeignKey('member.idmember'), primary_key=True)
    tasks_idtasks = db.Column(db.Integer, db.ForeignKey('tasks.idtasks'), primary_key=True)
    tasks_project_idproject = db.Column(db.Integer, primary_key=True)
    tasks_project_project_team_idproject_team = db.Column(db.Integer, primary_key=True)

class Domain(db.Model):
    __tablename__ = 'domain'
    iddomain = db.Column(db.Integer, primary_key=True)
    domain_name = db.Column(db.String(64))
    member_idmember = db.Column(db.Integer, db.ForeignKey('member.idmember'), nullable=False)

