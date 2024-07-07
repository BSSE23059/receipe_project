from .models import Student

students = Student.objects.all()


def addStudent():
    student_name = input("Enter name of student :")
    sage = input("Enter the age of student :")
    student_email = input("Enter email of student :")
    student_address = input("Enter address of student :")
    student = Student(name=student_name, age=sage, email=student_email, address=student_address)
    student.save()


def displayStudents():
    for student in students:
        print(str(student.id) + ". Name : " + student.name)
        print("Age : " + str(student.age))
        print("Email : " + student.email)
        print("Address : " + student.address)
        print("--------------------------")
