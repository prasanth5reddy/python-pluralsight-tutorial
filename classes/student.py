students = []


class Student:
    school_name = "Greenfield"  # similar to static variable

    def __init__(self, name, last_name, student_id=332):
        self.name = name
        self.last_name = last_name
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
