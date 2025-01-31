# Re-define the `Student` and `Instructor` classes and run the demonstration, as the execution environment was reset.

class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.assignments = {}

    def add_assignment(self, assignment_name, grade):
        """Adds an assignment and grade to the student's record."""
        self.assignments[assignment_name] = grade

    def display_grades(self):
        """Displays all assignments and grades for the student."""
        print(f"Grades for {self.name}:")
        if self.assignments:
            for assignment, grade in self.assignments.items():
                print(f"{assignment}: {grade}")
        else:
            print("No grades available.")


class Instructor:
    def __init__(self, name, course_name):
        self.name = name
        self.course_name = course_name
        self.students = []

    def add_student(self, student):
        """Adds a student to the course."""
        self.students.append(student)
        print(f"Student {student.name} (ID: {student.student_id}) has been added to {self.course_name}.")

    def assign_grade(self, student_id, assignment_name, grade):
        """Assigns a grade to a student for a specified assignment."""
        student = next((s for s in self.students if s.student_id == student_id), None)
        if student:
            student.add_assignment(assignment_name, grade)
            print(f"Assigned grade {grade} for '{assignment_name}' to {student.name}.")
        else:
            print(f"Student with ID {student_id} not found in {self.course_name}.")

    def display_students_grades(self):
        """Displays all students and their grades."""
        print(f"Grades for {self.course_name} course:")
        if self.students:
            for student in self.students:
                print(f"\nStudent: {student.name} (ID: {student.student_id})")
                student.display_grades()
        else:
            print("No students enrolled in this course.")


instructor = Instructor("Dr. Antoine", "Introduction to Marketing")
student1 = Student("Melissa", "S001")
student2 = Student("Elaine", "S002")

instructor.add_student(student1)
instructor.add_student(student2)

instructor.assign_grade("S001", "Assignment 1", 65)
instructor.assign_grade("S002", "Assignment 1", 72)
instructor.assign_grade("S001", "Assignment 2", 52)

instructor.display_students_grades()
