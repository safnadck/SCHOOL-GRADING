from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404
from .models import Student, Subject, Grade
from .forms import GradeForm

# List of all students
def student_list(request):
    students = Student.objects.all()
    return render(request, 'grades/student_list.html', {'students': students})

# List of all subjects
def subject_list(request):
    subjects = Subject.objects.all()
    return render(request, 'grades/subject_list.html', {'subjects': subjects})

# List of grades for a specific student
def student_grades(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    grades = Grade.objects.filter(student=student)
    return render(request, 'grades/student_grades.html', {'student': student, 'grades': grades})

# List of grades for a specific subject
def subject_grades(request, subject_id):
    subject = get_object_or_404(Subject, id=subject_id)
    grades = Grade.objects.filter(subject=subject)
    return render(request, 'grades/subject_grades.html', {'subject': subject, 'grades': grades})

# Add a grade for a student
def add_grade(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    if request.method == 'POST':
        form = GradeForm(request.POST)
        if form.is_valid():
            grade = form.save(commit=False)
            grade.student = student
            grade.save()
            return redirect('student_grades', student_id=student.id)
    else:
        form = GradeForm()
    return render(request, 'grades/add_grade_form.html', {'form': form, 'student': student})
