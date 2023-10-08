from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Project(db.Model):
    __tablename__ = 'project'
    idproject = db.Column(db.Integer, primary_key=True)
    project_name = db.Column(db.String(45), nullable=False)
    project_description = db.Column(db.String(255))
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    update_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    expired_at = db.Column(db.DateTime)
    status = db.Column(db.String(15), nullable=False)
    _idproject_team = db.Column(db.Integer, db.ForeignKey('project_team.idproject_team'), nullable=False)
    project_step = db.Column(db.Text)





class Meeting(db.Model):
    __tablename__ = 'meeting'
    idmeeting = db.Column(db.Integer, primary_key=True)
    meeting_subject = db.Column(db.String(45), nullable=False)
    meeting_time = db.Column(db.DateTime, nullable=False)
    meeting_members = db.Column(db.String(10))
    _idclient_user = db.Column(db.Integer, db.ForeignKey('client_user.idclient_user'), nullable=False)

class Resume(db.Model):
    __tablename__ = 'resume'
    idresume = db.Column(db.Integer, primary_key=True)
    resum_description = db.Column(db.String(45))
    _idproject = db.Column(db.Integer, db.ForeignKey('project.idproject'))
    _idproject_team = db.Column(db.Integer, db.ForeignKey('project_team.idproject_team'))
    
    project = db.relationship('Project', foreign_keys=[_idproject])
    project_team = db.relationship('ProjectTeam', foreign_keys=[_idproject_team])


class MeetingHasProjectTeam(db.Model):
    __tablename__ = 'meeting_has_project_team'
    meeting_idmeeting = db.Column(db.Integer, db.ForeignKey('meeting.idmeeting'), primary_key=True)
    project_team_idproject_team = db.Column(db.Integer, db.ForeignKey('project_team.idproject_team'), primary_key=True)
    
    meeting = db.relationship('Meeting', foreign_keys=[meeting_idmeeting])
    project_team = db.relationship('ProjectTeam', foreign_keys=[project_team_idproject_team])

class Comments(db.Model):
    __tablename__ = 'comments'
    idcomments = db.Column(db.Integer, primary_key=True)
    comments_lib = db.Column(db.Text)
    _idproject = db.Column(db.Integer, db.ForeignKey('project.idproject'))
    _idproject_team = db.Column(db.Integer, db.ForeignKey('project_team.idproject_team'))
    updated_at = db.Column(db.DateTime, server_default=db.func.current_timestamp())
    
    project = db.relationship('Project', foreign_keys=[_idproject])
    project_team = db.relationship('ProjectTeam', foreign_keys=[_idproject_team])


