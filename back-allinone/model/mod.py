from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Meeting(db.Model):
    __tablename__ = 'meeting'
    idmeeting = db.Column(db.Integer, primary_key=True)
    meeting_subject = db.Column(db.String(45), nullable=False)
    meeting_time = db.Column(db.DateTime, nullable=False)
    meeting_members = db.Column(db.String(10))
    _idclient_user = db.Column(db.Integer, db.ForeignKey('client_user.idclient_user'), nullable=False)


class MeetingHasProjectTeam(db.Model):
    __tablename__ = 'meeting_has_project_team'
    meeting_idmeeting = db.Column(db.Integer, db.ForeignKey('meeting.idmeeting'), primary_key=True)
    project_team_idproject_team = db.Column(db.Integer, db.ForeignKey('project_team.idproject_team'), primary_key=True)
    
    meeting = db.relationship('Meeting', foreign_keys=[meeting_idmeeting])
    project_team = db.relationship('ProjectTeam', foreign_keys=[project_team_idproject_team])


