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

