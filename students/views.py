from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from .models import Student
from .forms import StudentForm
from student_library.student_crud import *


def student_list(request):
    """
    Display a list of all student records.
    """
    return list(request)


def student_detail(request, pk):
    """
    Display the details of a single student record.
    """
    return detail(request, pk)


def student_create(request):
    return create(request)


def student_update(request, pk):
    """
    Update an existing student record.
    """
    return update(request, pk)


def student_delete(request, pk):
    """s
    Delete an existing student record.
    """
    return delete(request, pk)


def student_search(request):
    return search(request)
