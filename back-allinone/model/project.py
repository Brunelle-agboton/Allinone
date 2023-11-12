from app import db, bcrypt


class Project(db.Model):
    __tablename__ = 'project'

    idproject = db.Column(db.Integer, primary_key=True, autoincrement=True)
    project_name = db.Column(db.String(45), nullable=False)
    project_description = db.Column(db.String(255))
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    update_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    expired_at = db.Column(db.DateTime)
    project_status = db.Column(db.Integer, db.ForeignKey('status.idstatus'), nullable=False, default=1)
    _idproject_team = db.Column(db.Integer, db.ForeignKey('project_team.idproject_team'))
    project_step = db.Column(db.Text)
    requirement = db.Column(db.String(255))
    project_team_idproject_team = db.Column(db.Integer)
    client_user_idclient_user = db.Column(db.Integer)
    _idclient_user = db.Column(db.Integer, db.ForeignKey('client_user.idclient_user'))
    #id_status= db.Column(db.Integer,db.ForeignKey('project_status.idstatus'))
    
    # Définir les relations avec les autres tables
    project_team = db.relationship("ProjectTeam", back_populates="projects")
    client_user = db.relationship("ClientUser",  back_populates="project")
    status = db.relationship("Status", back_populates="projects")
    comments=db.relationship("Comments", back_populates="project")
    tasks = db.relationship("Tasks", back_populates="project")
    resumes=db.relationship("Resume", back_populates="project")
    # meetings=db.Column("Meeting", back_populates="project")
    
class Meeting(db.Model):
    __tablename__ = 'meeting'

    idmeeting = db.Column(db.Integer, primary_key=True, autoincrement=True)
    meeting_subject = db.Column(db.String(45), nullable=False)
    meeting_time = db.Column(db.DateTime, nullable=False)
    meeting_members = db.Column(db.String(255))
    _idclient_user = db.Column(db.Integer, db.ForeignKey('client_user.idclient_user'), nullable=False)
    project_idproject = db.Column(db.Integer, db.ForeignKey('project.idproject'), nullable=False)
    project_team_idproject_team = db.Column(db.Integer, db.ForeignKey('project_team.idproject_team'), nullable=False)
    project_client_user_idclient_user = db.Column(db.Integer, db.ForeignKey('client_user.idclient_user'), nullable=False)

    client_user = db.relationship("ClientUser", primaryjoin="Meeting._idclient_user == ClientUser.idclient_user", back_populates="meetings")
    # project = db.relationship("Project", back_populates="meetings")
    project_team = db.relationship("ProjectTeam", back_populates="meetings")

class ClientUser(db.Model):
    __tablename__ = 'client_user'

    idclient_user = db.Column(db.Integer, primary_key=True, autoincrement=True)
    client_user_name = db.Column(db.String(45), nullable=False)
    client_email = db.Column(db.String(64), nullable=False)
    client_user_activity = db.Column(db.String(45))
    client_user_no = db.Column(db.String(45))
    _idclient_address = db.Column(db.Integer, db.ForeignKey('client_address.idclient_address'), nullable=False)
    _idrole = db.Column(db.Integer, db.ForeignKey('role.idrole'), nullable=False,)

    project = db.relationship("Project", back_populates="client_user")  # Relation avec la table "project"
    client_address = db.relationship("ClientAddress", back_populates="client_users")
    role = db.relationship("Role", back_populates="client_users")
    # comments = db.relationship("Comments", back_populates="client_user")
    meetings = db.relationship("Meeting",primaryjoin="ClientUser.idclient_user == Meeting._idclient_user", back_populates="client_user")
    #tasks = db.relationship("Tasks", secondary='tasks_has_client_user', back_populates="client_users")

class ClientAddress(db.Model):
    __tablename__ = 'client_address'

    idclient_address = db.Column(db.Integer, primary_key=True)
    client_street = db.Column(db.String(255))
    client_city = db.Column(db.String(45), nullable=False)
    client_state = db.Column(db.String(45), nullable=False)
    client_postal_code = db.Column(db.String(45))
    
    client_users = db.relationship("ClientUser", back_populates="client_address")
    
class Comments(db.Model):
    __tablename__ = 'comments'

    idcomments = db.Column(db.Integer, primary_key=True, autoincrement=True)
    comments_lib = db.Column(db.Text)
    updated_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    project_idproject = db.Column(db.Integer, db.ForeignKey('project.idproject'), nullable=False)

    project = db.relationship("Project", back_populates="comments")

class Status(db.Model):
    __tablename__ = 'status'

    idstatus = db.Column(db.Integer, primary_key=True, autoincrement=True)
    status_name = db.Column(db.String(45))

    projects = db.relationship("Project", back_populates="status")
    tasks=db.relationship("Tasks", back_populates="status")
       
class ProjectTeam(db.Model):
    __tablename__ = 'project_team'

    idproject_team = db.Column(db.Integer, primary_key=True, autoincrement=True)
    team_name = db.Column(db.String(45))
    team_description = db.Column(db.String(64))
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    last_modified = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    
    # Définir les relations avec les autres tables
    members = db.relationship("Member", secondary='project_team_has_member', back_populates="teams")
    projects = db.relationship("Project", back_populates="project_team")
    meetings=db.relationship("Meeting", back_populates="project_team")
    tasks=db.relationship("Tasks", back_populates="project_team")

class Member(db.Model):
    __tablename__ = 'member'

    idmember = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(16), nullable=False)
    email = db.Column(db.String(255))
    password = db.Column(db.String(64), nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    
    def set_password(self, passw):
        self.password = bcrypt.generate_password_hash(passw).decode('utf-8')

    def check_password(self, passw):
        return bcrypt.check_password_hash(self.password, passw)


    roles = db.relationship("Role", secondary='member_has_role', back_populates="members")
    domains = db.relationship("Domain", secondary='member_has_domain', back_populates="members")
    tasks = db.relationship("Tasks", secondary='member_has_tasks', back_populates="members", secondaryjoin="Member.idmember == member_has_tasks.c.member_idmember")

    teams=db.relationship("ProjectTeam", secondary='project_team_has_member', back_populates="members")
    
class ProjectTeamHasMember(db.Model):
    __tablename__ = 'project_team_has_member'

    project_team_idproject_team = db.Column(db.Integer, db.ForeignKey('project_team.idproject_team'), primary_key=True)
    member_idmember = db.Column(db.Integer, db.ForeignKey('member.idmember'), primary_key=True)

    # Vous n'avez pas besoin de définir de relation ici car elle est gérée via 'members' dans ProjectTeam et 'teams' dans Member.

class Role(db.Model):
    __tablename__ = 'role'

    idrole = db.Column(db.Integer, primary_key=True, autoincrement=True)
    super_admin = db.Column(db.Boolean)
    admin = db.Column(db.Boolean)
    user = db.Column(db.Boolean)
    client = db.Column(db.Boolean)

    client_users = db.relationship("ClientUser", back_populates="role")
    members = db.relationship("Member", secondary='member_has_role', back_populates="roles")


class Tasks(db.Model):
    __tablename__ = 'tasks'

    idtasks = db.Column(db.Integer, primary_key=True, autoincrement=True)
    tasks_description = db.Column(db.String(255), nullable=False)
    added_at = db.Column(db.Date, nullable=False)
    finished_at = db.Column(db.Date, nullable=False)
    _idproject_team = db.Column(db.Integer, nullable=False)
    status_idstatus = db.Column(db.Integer, db.ForeignKey('status.idstatus'), nullable=False)
    project_project_team_idproject_team1 = db.Column(db.Integer, db.ForeignKey('project_team.idproject_team'), nullable=False)
    project_client_user_idclient_user1 = db.Column(db.Integer, db.ForeignKey('client_user.idclient_user'), nullable=False)
    member_idmember = db.Column(db.Integer, db.ForeignKey('member.idmember'))
    project_idproject=db.Column(db.Integer, db.ForeignKey('project.idproject'))
    
    project = db.relationship("Project", foreign_keys=[project_idproject], back_populates="tasks")

    project_team = db.relationship("ProjectTeam", back_populates="tasks")
    status = db.relationship("Status", back_populates="tasks")
    members = db.relationship("Member", secondary='member_has_tasks', back_populates="tasks", primaryjoin="Tasks.idtasks == member_has_tasks.c.tasks_idtasks")
#client_users = db.relationship("ClientUser", back_populates="tasks")

class MemberHasTasks(db.Model):
    __tablename__ = 'member_has_tasks'

    member_idmember = db.Column(db.Integer, db.ForeignKey('member.idmember'), primary_key=True)
    tasks_idtasks = db.Column(db.Integer, primary_key=True)
    tasks_project_idproject1 = db.Column(db.Integer, primary_key=True)

    # Vous n'avez pas besoin de définir de relation ici car elle est gérée via 'tasks' dans Member et 'members' dans Task.

class Domain(db.Model):
    __tablename__ = 'domain'
    iddomain = db.Column(db.Integer, primary_key=True, autoincrement=True)
    domain_name = db.Column(db.String(64))
    member_idmember = db.Column(db.Integer, db.ForeignKey('member.idmember'), nullable=False)
    
    members = db.relationship("Member", secondary='member_has_domain', back_populates="domains")

class Resume(db.Model):
    __tablename__ = 'resume'

    idresume = db.Column(db.Integer, primary_key=True, autoincrement=True)
    resum_description = db.Column(db.String(45), nullable=False)
    project_idproject = db.Column(db.Integer, db.ForeignKey('project.idproject'), nullable=False)

    # Définir la relation avec la table Project
    project = db.relationship("Project", back_populates="resumes")

class MemberHasRole(db.Model):
    __tablename__ = 'member_has_role'

    member_idmember = db.Column(db.Integer, db.ForeignKey('member.idmember'), primary_key=True)
    role_idrole = db.Column(db.Integer, db.ForeignKey('role.idrole'), primary_key=True)

    # Vous n'avez pas besoin de définir de relation ici car elle est gérée via 'roles' dans Member et 'members' dans Role.

class MemberHasDomain(db.Model):
    __tablename__ = 'member_has_domain'

    member_idmember = db.Column(db.Integer, db.ForeignKey('member.idmember'), primary_key=True)
    domain_iddomain = db.Column(db.Integer, db.ForeignKey('domain.iddomain'), primary_key=True)

    # Vous n'avez pas besoin de définir de relation ici car elle est gérée via 'domains' dans Member et 'members' dans Domain.

