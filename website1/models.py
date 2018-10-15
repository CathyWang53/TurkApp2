from website1 import db

class ResultTable(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    answer = db.Column(db.Text(), nullable=False)
    extend_existing=True

    def __repr__(self):
        return '<ResultTable: {}>'.format(self.name)

class Results(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    userid=db.Column(db.Text(),nullable=False)
    text = db.Column(db.Text(), nullable=False)
    mp3url = db.Column(db.Text(), nullable=False)
    queryname = db.Column(db.Text(), nullable=False)

    def __repr__(self):
        return '<Results: {}>'.format(self.name)

class feedbacks(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    userid=db.Column(db.Text(), nullable=False)
    feedback = db.Column(db.Text(), nullable=False)
    duration = db.Column(db.Integer, nullable=False)
    version = db.Column(db.Text(), nullable=False)

    def __repr__(self):
        return '<feedbacks: {}>'.format(self.name)

class results_ver_game(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    userid=db.Column(db.Text(),nullable=False)
    text = db.Column(db.Text(), nullable=False)
    mp3url = db.Column(db.Text(), nullable=False)
    queryname = db.Column(db.Text(), nullable=False)
    answerTime = db.Column(db.Integer, nullable=False)
    answertime2 = db.Column(db.Integer)
    datetime = db.Column(db.Text())
    category = db.Column(db.Text())

    def __repr__(self):
        return '<results_ver_game: {}>'.format(self.name)

# class feedbacks_ver_game(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     userid=db.Column(db.Text(),nullable=False)
#     feedback = db.Column(db.Text(), nullable=False)
#     duration = db.Column(db.Integer, nullable=False)
#
#     def __repr__(self):
#         return '<feedbacks_ver_game: {}>'.format(self.name)

class results_ver_easy(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    userid=db.Column(db.Text(),nullable=False)
    text = db.Column(db.Text(), nullable=False)
    mp3url = db.Column(db.Text(), nullable=False)
    queryname = db.Column(db.Text(), nullable=False)

    def __repr__(self):
        return '<results_ver_easy: {}>'.format(self.name)

# class feedbacks_ver_easy(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     userid=db.Column(db.Text(),nullable=False)
#     feedback = db.Column(db.Text(), nullable=False)
#     duration = db.Column(db.Integer, nullable=False)
#
#     def __repr__(self):
#         return '<feedbacks_ver_easy: {}>'.format(self.name)
