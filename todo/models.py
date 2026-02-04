from .app import db

class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200))
    questionnaire_id = db.Column(db.Integer, db.ForeignKey('questionnaire.id'))
    type = db.Column(db.String(50)) 

    __mapper_args__ = {
        'polymorphic_identity': 'question',
        'polymorphic_on': type
    }

    def to_json(self, index):
        return {
            'id': self.id,
            'number': index,
            'title': self.title,
            'type': self.type
        }

class QuestionOuverte(Question):
    id = db.Column(db.Integer, db.ForeignKey('question.id'), primary_key=True)
    reponse = db.Column(db.String(200))

    __mapper_args__ = {
        'polymorphic_identity': 'ouverte',
    }

    def to_json(self, index):
        json = super().to_json(index)
        json['reponse'] = self.reponse
        return json

class QuestionQCM(Question):
    id = db.Column(db.Integer, db.ForeignKey('question.id'), primary_key=True)
    p1 = db.Column(db.String(200))
    p2 = db.Column(db.String(200))
    bonne_reponse = db.Column(db.Integer)

    __mapper_args__ = {
        'polymorphic_identity': 'qcm',
    }

    def to_json(self, index):
        json = super().to_json(index)
        json.update({
            'p1': self.p1,
            'p2': self.p2,
            'bonne_reponse': self.bonne_reponse
        })
        return json

class Questionnaire(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    questions = db.relationship("Question", backref="questionnaire", cascade="all, delete-orphan")

    def to_json(self):
        return { 'id': self.id, 'name': self.name }
    
    def delete_question(self, question_id):
        question = Question.query.filter_by(id=question_id, questionnaire_id=self.id).first()
        if question:
            db.session.delete(question)
            db.session.commit()
            return True
        return False

def get_all_questionnaires():
    return Questionnaire.query.all()

def get_questionnaire_by_id(qid):
    return Questionnaire.query.get(qid)

def create_questionnaire(name):
    new_q = Questionnaire(name=name)
    db.session.add(new_q)
    db.session.commit()
    return new_q

def delete_questionnaire(qid):
    q = Questionnaire.query.get(qid)
    if q:
        db.session.delete(q)
        db.session.commit()