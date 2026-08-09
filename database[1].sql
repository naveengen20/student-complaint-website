CREATE TABLE complaints (
    complaint_id INTEGER PRIMARY KEY,
    student_name TEXT NOT NULL,
    year TEXT NOT NULL,
    department TEXT NOT NULL,
    complaint_about TEXT NOT NULL,
    details TEXT NOT NULL
);
