CREATE TABLE Grades (
    grade       number(3),
    student_id  number(5) NOT NULL,
    course_id   varchar2(255) NOT NULL,
    CONSTRAINT grade_pk PRIMARY KEY (student_id, course_id),
    CONSTRAINT student_fk FOREIGN KEY (student_id) REFERENCES students(id),
    CONSTRAINT course_fk FOREIGN KEY (course_id) REFERENCES courses(course_id));
