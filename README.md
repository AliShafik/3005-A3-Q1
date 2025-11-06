# 3005-A3-Q1

Ali Shafik
101260471

Video Link:
https://youtu.be/BahYXprvhVA

## Setup:
pip install psycopg2

Open PostgreSQL and create a new database:

CREATE DATABASE school;

In the `school` database, create the `students` table:

CREATE TABLE students (
    student_id SERIAL PRIMARY KEY,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    enrollment_date DATE
);

INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES
('John', 'Doe', 'john.doe@example.com', '2023-09-01'),
('Jane', 'Smith', 'jane.smith@example.com', '2023-09-01'),
('Jim', 'Beam', 'jim.beam@example.com', '2023-09-02');

In `crud.py` change the config password and username to your own login for postgres.

Run 'python crud.py'