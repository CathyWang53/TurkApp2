from website1 import db

class ResultTable(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    answer = db.Column(db.Text(), nullable=False)
    
    def __repr__(self):
        return '<ResultTable: {}>'.format(self.name)

class Results(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text(), nullable=False)
    Mp3url = db.Column(db.Text(), nullable=False)
    queryname = db.Column(db.Text(), nullable=False)
    
    def __repr__(self):
        return '<Results: {}>'.format(self.name)
