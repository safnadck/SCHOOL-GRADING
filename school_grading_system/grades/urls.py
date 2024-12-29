from django.urls import path
from . import views

urlpatterns = [
    path('', views.student_list, name='student_list'),
    path('subjects/', views.subject_list, name='subject_list'),
    path('student/<int:student_id>/grades/', views.student_grades, name='student_grades'),
    path('subject/<int:subject_id>/grades/', views.subject_grades, name='subject_grades'),
    path('grade/<int:student_id>/add/', views.add_grade, name='add_grade'),
]
