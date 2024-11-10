from django.shortcuts import render, redirect
import pyrebase

# Firebase Configuration
config = {
    "apiKey": "AIzaSyDDSTV6cYvitI0iMTEvwrAaT49gMNqWuMo",
    "authDomain": "test-7eddd.firebaseapp.com",
    "databaseURL": "https://test-7eddd-default-rtdb.firebaseio.com",
    "projectId": "test-7eddd",
    "storageBucket": "test-7eddd.firebasestorage.app",
    "messagingSenderId": "216594930584",
    "appId": "1:216594930584:web:04df16573918477dbd29ed",
}

firebase = pyrebase.initialize_app(config)
database = firebase.database()

# Home Page: List all students
def index(request):
    students = database.child('students').get().val()
    students = students if students else {}
    return render(request, 'index.html', {'students': students})

# Add a new student
def add_student(request):
    if request.method == 'POST':
        name = request.POST['name']
        subject = request.POST['subject']
        subject_code = request.POST['subject_code']  # Get subject code from form
        usn = request.POST['usn']
        semester = request.POST['semester']
        marks = request.POST['marks']
        faculty = request.POST['faculty']

        student_data = {
            'name': name,
            'subject': subject,
            'subject_code': subject_code,  # Include subject code
            'usn': usn,
            'semester': semester,
            'marks': marks,
            'faculty': faculty
        }

        # Push new student data to Firebase
        database.child('students').push(student_data)

        return redirect('index')

    return render(request, 'add_student.html')

# Edit student information
def edit_student(request, student_id):
    student = database.child('students').child(student_id).get().val()

    if request.method == 'POST':
        name = request.POST['name']
        subject = request.POST['subject']
        subject_code = request.POST['subject_code']  # Get subject code from form
        usn = request.POST['usn']
        semester = request.POST['semester']
        marks = request.POST['marks']
        faculty = request.POST['faculty']

        student_data = {
            'name': name,
            'subject': subject,
            'subject_code': subject_code,  # Include subject code
            'usn': usn,
            'semester': semester,
            'marks': marks,
            'faculty': faculty
        }

        # Update student data in Firebase
        database.child('students').child(student_id).update(student_data)

        return redirect('index')

    return render(request, 'edit_student.html', {'student': student})

# Delete student record
def delete_student(request, student_id):
    # Delete student from Firebase
    database.child('students').child(student_id).remove()

    return redirect('index')
