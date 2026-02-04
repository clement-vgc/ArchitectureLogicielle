from .app import app, db
from .models import Questionnaire, QuestionOuverte, QuestionQCM

@app.cli.command()
def syncdb():
    """Initialise la base de données avec 3 questionnaires qui ont entre 2 et 3 questions"""
    db.drop_all() 
    db.create_all()

    q1 = Questionnaire(name='Géographie')
    db.session.add(q1)
    db.session.commit()

    db.session.add_all([
        QuestionOuverte(title="Quelle est la capitale du Japon ?", reponse="Tokyo", questionnaire_id=q1.id),
        QuestionQCM(title="Quel est le plus grand océan ?", p1="Atlantique", p2="Pacifique", bonne_reponse=2, questionnaire_id=q1.id),
        QuestionOuverte(title="Quel fleuve traverse Paris ?", reponse="La Seine", questionnaire_id=q1.id)
    ])

    q2 = Questionnaire(name='Histoire')
    db.session.add(q2)
    db.session.commit()

    db.session.add_all([
        QuestionQCM(title="En quelle année a eu lieu la Révolution Française ?", p1="1789", p2="1914", bonne_reponse=1, questionnaire_id=q2.id),
        QuestionOuverte(title="Qui était surnommé le Roi-Soleil ?", reponse="Louis XIV", questionnaire_id=q2.id)
    ])

    q3 = Questionnaire(name='Sciences')
    db.session.add(q3)
    db.session.commit()

    db.session.add_all([
        QuestionOuverte(title="Quel est le symbole chimique de l'eau ?", reponse="H2O", questionnaire_id=q3.id),
        QuestionQCM(title="La Terre est-elle plate ?", p1="Vrai", p2="Faux", bonne_reponse=2, questionnaire_id=q3.id),
        QuestionOuverte(title="Quelle planète est appelée la planète rouge ?", reponse="Mars", questionnaire_id=q3.id)
    ])
    db.session.commit()
    print("Base de données initialisée !")