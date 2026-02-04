from flask import jsonify, abort, make_response, request, url_for, redirect
from .app import app, db
from .models import (
    get_all_questionnaires, get_questionnaire_by_id, 
    create_questionnaire, delete_questionnaire,
    Question, QuestionOuverte, QuestionQCM
)

def make_public_questionnaire(quiz):
    new_quiz = {}
    quiz_data = quiz.to_json()
    for field in quiz_data:
        if field == 'id':
            new_quiz['uri'] = url_for('get_one_questionnaire', qid=quiz_data['id'], _external=True)
        else:
            new_quiz[field] = quiz_data[field]
    return new_quiz


@app.route('/')
def home():
    return redirect(url_for('get_questionnaires'))

@app.route('/quiz/api/v1.0/questionnaires', methods=['GET'])
def get_questionnaires():
    return jsonify({'questionnaires': [make_public_questionnaire(q) for q in get_all_questionnaires()]})

@app.route('/quiz/api/v1.0/questionnaires/<int:qid>', methods=['GET', 'PUT', 'DELETE'])
def get_one_questionnaire(qid):
    q = get_questionnaire_by_id(qid)
    if q is None:
        abort(404)

    if request.method == 'PUT':
        if not request.json or 'name' not in request.json:
            abort(400)
        q.name = request.json['name']
        db.session.commit()
        return jsonify({'questionnaire': make_public_questionnaire(q)})

    if request.method == 'DELETE':
        delete_questionnaire(qid)
        return jsonify({'status': 'deleted'})

    return jsonify({'questionnaire': make_public_questionnaire(q)})

@app.route('/quiz/api/v1.0/questionnaires', methods=['POST'])
def add_questionnaire():
    if not request.json or 'name' not in request.json:
        abort(400)
    new_q = create_questionnaire(request.json['name'])
    if new_q is None:
        return make_response(jsonify({'error': 'Ce nom de questionnaire existe déjà'}), 409)
    return jsonify({'questionnaire': make_public_questionnaire(new_q)}), 201

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

@app.errorhandler(400)
def bad_request(error):
    return make_response(jsonify({'error': 'Bad request'}), 400)

@app.route('/quiz/api/v1.0/questionnaires/<int:qid>/questions/<int:quid>', methods=['PUT'])
def update_question(qid, quid):
    q = get_questionnaire_by_id(qid)
    if q is None:
        abort(404)
    
    question = Question.query.filter_by(id=quid, questionnaire_id=qid).first()
    if question is None:
        abort(404)
        
    data = request.json
    if not data:
        abort(400)
    question.title = data.get('title', question.title)

    if isinstance(question, QuestionOuverte):
        question.reponse = data.get('reponse', question.reponse)
    elif isinstance(question, QuestionQCM):
        question.p1 = data.get('p1', question.p1)
        question.p2 = data.get('p2', question.p2)
        question.bonne_reponse = data.get('bonne_reponse', question.bonne_reponse)

    db.session.commit()
    return jsonify({'question': question.to_json(0)})

@app.route('/quiz/api/v1.0/questionnaires/<int:qid>', methods=['DELETE'])
def remove_questionnaire(qid):
    q = get_questionnaire_by_id(qid)
    if q is None:
        abort(404)
    delete_questionnaire(qid)
    return jsonify({'status': 'deleted'})

@app.route('/quiz/api/v1.0/questionnaires/<int:qid>/questions', methods=['GET'])
def get_questions(qid):
    q = get_questionnaire_by_id(qid)
    if q is None:
        abort(404)
    return jsonify({
        'questions': [quest.to_json(i) for i, quest in enumerate(q.questions)]
    })

@app.route('/quiz/api/v1.0/questionnaires/<int:qid>/questions', methods=['POST'])
def add_question_to_quiz(qid):
    q = get_questionnaire_by_id(qid)
    if q is None:
        abort(404)
    if not request.json or 'title' not in request.json:
        abort(400)
    
    data = request.json
    
    if 'reponse' in data:
        new_quest = QuestionOuverte(
            title=data['title'], 
            reponse=data['reponse'], 
            questionnaire_id=qid
        )
    elif 'p1' in data and 'p2' in data:
        new_quest = QuestionQCM(
            title=data['title'], 
            p1=data['p1'], 
            p2=data['p2'], 
            bonne_reponse=data.get('bonne_reponse', 1), 
            questionnaire_id=qid
        )
    else:
        new_quest = Question(title=data['title'], questionnaire_id=qid)

    try:
        db.session.add(new_quest)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        abort(500)
    return jsonify({'question': new_quest.to_json(len(q.questions)-1)}), 201

@app.route('/quiz/api/v1.0/questionnaires/<int:qid>/questions/<int:quid>', methods=['DELETE'])
def remove_question(qid, quid):
    q = get_questionnaire_by_id(qid)
    if q is None:
        abort(404)
    
    if not q.delete_question(quid):
        abort(404)
        
    return jsonify({'status': 'deleted'})

@app.route('/quiz/api/v1.0/questionnaires/<int:qid>/questions/<int:quid>', methods=['GET'])
def get_one_question(qid, quid):
    q = get_questionnaire_by_id(qid)
    if q is None:
        abort(404)
    
    question = Question.query.filter_by(id=quid, questionnaire_id=qid).first()
    
    if question is None:
        abort(404)
        
    return jsonify({'question': question.to_json(0)})