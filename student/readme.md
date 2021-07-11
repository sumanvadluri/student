## STUDENT MARKS INFO PROJECT:

To run this application follows the below steps:

1.create an virtual enviornment for this project.By running "python -m venv env" command
2.activate enviornment.by running ".\env\scripts\activate"
3.To install all required packages for this project, Run "pip install -r requirements.txt"
4.Run python manage.py makemigrations
5.Run python manage.py migrate
6.Run python manage.py runserver
Note: For this project default database sqlite3 was used.

To access this application, call below api's:

1. POST: http://127.0.0.1:8000/api/marks -->To create marks for a student.
2. GET: http://127.0.0.1:8000/api/marks -->To get marks for all students.
3. GET: http://127.0.0.1:8000/api/marks/<int:id> -->To get marks for a perticular student.
4. GET: http://127.0.0.1:8000/api/student/marks -->To get total marks for all students.
5. GET: http://127.0.0.1:8000/api/subject/average -->To get average marks of a all student for each subject.

Thankyou.
