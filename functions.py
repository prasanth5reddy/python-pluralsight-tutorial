# variable arguments
def var_args(name, *args):
    print(name)
    print(args)


def var_kwargs(name, **kwargs):
    print(name)
    print(kwargs)
    print(kwargs["description"])


var_args("Mark", "Loves Python", None, "Hello", True)
var_kwargs("Marks", description="Loves Python", feedback=None, subscription=True)
print()

# lambda functions
double = lambda x: x * 2
print(double(5), "\n")

# students list
students = []


def get_students_titlecase():
    students_titlecase = []
    for student in students:
        students_titlecase.append(student["name"].title())
    return students_titlecase


def print_students_titlecase():
    students_titlecase = get_students_titlecase()
    print(students_titlecase)


def add_student(name, student_id=332):
    student = {"name": name, "student_id": student_id}
    students.append(student)


def save_file(student):
    try:
        f = open("students.txt", "a")
        f.write(student + "\n")
        f.close()
    except Exception:
        print("Could not save file")


def read_file():
    try:
        f = open("students.txt", "r")
        # for student in f.readlines():
        for student in read_students(f):
            add_student(student)
        f.close()
    except Exception:
        print("Could not read file")


# yield functions
def read_students(file):
    for line in file:
        yield line


read_file()
print_students_titlecase()

student_name = input("Enter student name : ")
student_id = input("Enter student id : ")

add_student(student_name, int(student_id))

print_students_titlecase()
save_file(student_name)
