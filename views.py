from django.shortcuts import render, redirect
from Curd_app.models import Student
from django.contrib import messages


def student(request):
    n = ''  # Message to display
    if request.method == "POST":
        name = request.POST.get('name')
        student_class = request.POST.get('sclass')
        fname = request.POST.get('fathername')
        phone = request.POST.get('phone')

        if name:  # Ensure name is not empty
            std = Student(name=name, student_class=student_class, fathername=fname, phone=phone)
            std.save()
            n = 'Data saved successfully!'  # Message to display after saving
        else:
            n = 'Name is required!'  # Message if name is empty

    # Query all student records
    students = Student.objects.all()

    # Pass the student records and message to the template
    data = {
        'std': students,
        'n': n,
    }

    return render(request, 'index.html', data)

def delete_student(request, student_id):
    try:
        student = Student.objects.get(id=student_id)
        student.delete()
        messages.success(request, 'Student record deleted successfully!')
    except Student.DoesNotExist:
        messages.error(request, 'Student record does not exist.')

    return redirect('/')

