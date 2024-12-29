from django.db import models

class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    email = models.EmailField()
    enrollment_date = models.DateTimeField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Subject(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=20)
    teacher_name = models.CharField(max_length=100)
    credits = models.IntegerField()

    def __str__(self):
        return self.name

class Grade(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    grade = models.CharField(max_length=2)
    score = models.DecimalField(max_digits=5, decimal_places=2)
    semester = models.CharField(max_length=20)
    date_awarded = models.DateField()

    def __str__(self):
        return f"{self.student} - {self.subject} - {self.grade}"
