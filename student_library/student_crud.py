from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from students.models import Student
from students.forms import StudentForm

def create(request):
    """
    Create a new student record.
    """
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("students:list")
    else:
        form = StudentForm()
    return render(request, "form.html", {"form": form})
    
def update(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == "POST":
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect("students:list")
    else:
        form = StudentForm(instance=student)
    return render(request, "form.html", {"form": form})
    
def delete(request, pk):
    """
    Delete an existing student record.
    """
    student = get_object_or_404(Student, pk=pk)
    student.delete()
    return redirect("students:list")
    
def search(request):
    query = request.GET.get("query", "")
    if not query:
        error_message = "Please enter a search query."
        students = Student.objects.all()
        return render(request, "list.html", {"error_message": error_message, "students": students})
    students = Student.objects.filter(
        Q(first_name__icontains=query) | Q(last_name__icontains=query) | Q(email__icontains=query)
    )
    return render(request, "list.html", {"students": students})
    
def detail(request, pk):
    """
    Display the details of a single student record.
    """
    student = get_object_or_404(Student, pk=pk)
    return render(request, "detail.html", {"student": student})
    
def list(request):
    """
    Display a list of all student records.
    """
    students = Student.objects.all()
    return render(request, "list.html", {"students": students})