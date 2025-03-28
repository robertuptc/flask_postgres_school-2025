from flask import Flask, jsonify
from models import Students, Teachers, Subjects, db
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://robert@localhost/school_db_2025'
app.json.sort_keys= False

db.init_app(app)

@app.route('/students/', methods=['GET'])
def get_students():
    students_list = []
    
    for stud in Students.query.all():
        individual = {
            'id': stud.id,
            'first_name': stud.first_name,
            'last_name': stud.last_name,
            'age': stud.age,
            'class': {
                'subject': stud.subjects.subject_name,
                'teacher:' : f"{stud.subjects.teachers[0].first_name} {stud.subjects.teachers[0].last_name}"
            }
        }
        students_list.append(individual)
    return jsonify(students_list)


@app.route('/teachers/', methods=['GET'])
def get_teachers():
    teachers_list = []
    for teacher in Teachers.query.all():
        individual = {
            'first_name': teacher.first_name,
            'last_name': teacher.last_name,
            'age': teacher.age,
            "subject" : {
                'subject': teacher.subjects.subject_name,
                'students': [f"{stud.first_name} {stud.last_name}" for stud in teacher.subjects.students]
            }
        }
        teachers_list.append(individual)
    return jsonify(teachers_list)

@app.route('/subjects/', methods=['GET'])
def get_subjects():
    subject_list = []
    for subject in Subjects.query.all():
        # for teacher in subject.teachers:
        #     print(teacher)
        subject_dict = {
            'teacher:': [f"{teacher.first_name} {teacher.last_name}" for teacher in subject.teachers],
            'students': [f"{stud.first_name} {stud.last_name}" for stud in subject.students]
        }
        print(subject_dict)
        subject_list.append(subject_dict)
    return jsonify(subject_list)
if __name__ == '__main__':
    app.run(debug=True, port=8000)