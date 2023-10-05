from app import db

class Project(db.Model):
    __tablename__ = 'project'
    idproject = db.Column(db.Integer, primary_key=True)
    project_name = db.Column(db.String(45), nullable=False)
    project_description = db.Column(db.String(255))
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    update_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    expired_at = db.Column(db.DateTime)
    status = db.Column(db.String(15), nullable=False)
    _idproject_team = db.Column(db.Integer, db.ForeignKey('project_team.idproject_team'), nullable=True)
    project_step = db.Column(db.Text)
    Requirement = db.Column(db.String(255), nullable=True)
