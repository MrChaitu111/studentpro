from django.shortcuts import render,redirect, get_object_or_404
from .models import Student
from django.contrib import messages
from .forms import StudentForm

# Create your views here.
def home(request):
    return render(request,'studentapp/index.html')

def add_student(request):
    students = Student.objects.all()
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Add Student Record successfully!")
            return redirect('add_student')
    else:
        form = StudentForm()
    return render(request, 'studentapp/student_form.html', {'form': form, 'students': students})
    

def edit_student(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == "POST":
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            messages.success(request, "Student updated successfully!")
            return redirect('add_student')
    else:
        form = StudentForm(instance=student)
    return render(request, 'studentapp/student_edit.html', {'form': form, 'student': student})


def view_students(request):
    students = Student.objects.all()
    return render(request, 'studentapp/view_students.html', {'students': students})

def about(request):
    return render(request, 'studentapp/about.html')

def contact(request):
    return render(request, 'studentapp/contact.html')

def delete_student(request, id):
    student = Student.objects.get(pk=id)
    student.delete()
    return redirect('view_students')
