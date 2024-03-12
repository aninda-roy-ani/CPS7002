from person import Person


class Classroom:

    def __init__(self, students=None, teacher=None):
        self.students = students if students else []
        self.teacher = teacher

    def add_student(self, student):
        self.students.append(student)

    def remove_student(self, student):
        self.students.remove(student)

    def assign_teacher(self, teacher):
        self.teacher = teacher

    def display_information(self):
        print("Teacher Information:")
        print(self.teacher.get_information())
        print("Students Information:")
        for student in self.students:
            print(student.get_information())

# Example usage:
teacher = Person("John Doe", 35, "T123")
teacher.set_contact_info("123 Main St", "john@example.com", "123-456-7890")
students = [Person("Alice", 18, "S001"), Person("Bob", 17, "S002")]
classroom = Classroom(students, teacher)
classroom.display_information()