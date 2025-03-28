DROP TABLE IF EXISTS students, teachers, subjects;

CREATE TABLE subjects(
    id serial PRIMARY KEY,
    subject_name VARCHAR(30)
);

CREATE TABLE students(
    id serial PRIMARY KEY,
    first_name VARCHAR(10),
    last_name VARCHAR(10),
    age INT,
    subject_id INT,
    FOREIGN KEY (subject_id) REFERENCES subjects(id)
);

CREATE TABLE teachers(
    id serial PRIMARY KEY,
    first_name VARCHAR(10),
    last_name VARCHAR(10),
    age INT,
    subject_id INT,
    FOREIGN KEY (subject_id) REFERENCES subjects(id)

);



\COPY subjects FROM '/Users/robert/Documents/Software Engineer/week3/day3/assigments/flask_postgres_school/data/subjects.csv' DELIMITER ',' CSV HEADER;
\COPY students FROM '/Users/robert/Documents/Software Engineer/week3/day3/assigments/flask_postgres_school/data/student.csv' DELIMITER ',' CSV HEADER;
\COPY teachers FROM '/Users/robert/Documents/Software Engineer/week3/day3/assigments/flask_postgres_school/data/teachers.csv' DELIMITER ',' CSV HEADER;
