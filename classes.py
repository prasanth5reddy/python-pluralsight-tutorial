class Example:
    pass  # tell interpreter to do nothing


example = Example()
print(example, "\n")

students = []


class Student:
    school_name = "Greenfield"  # similar to static variable

    def __init__(self, name, student_id=332):
        self.name = name
        self.student_id = student_id
        students.append(self)
        # student = {"name": name, "student_id": student_id}
        # students.append(student)

    def __str__(self):
        return "Student " + self.name

    def get_name_capitalize(self):
        return self.name.capitalize()

    def get_school_name(self):
        return self.school_name

    def _get_student_id(self):  # underscore prefix to tell developer this shouldn't be overridden or used directly
        return self.student_id


mark = Student("mark ruffalo")
print(mark)
print(mark.get_name_capitalize())
print(mark._get_student_id())  # Avoid using this
print(mark.get_school_name(), mark.school_name, Student.school_name)

print(students, "\n")


class HighSchoolStudent(Student):
    school_name = "Springfield"

    def get_school_name(self):
        # return super().school_name
        return self.school_name

    def get_name_capitalize(self):
        original_value = super().get_name_capitalize()
        return original_value + "-HS"


james = HighSchoolStudent("james")
print(james.get_name_capitalize())
print(james.get_school_name())
