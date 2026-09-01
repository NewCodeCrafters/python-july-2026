class Course_Registration_System():
    def __init__(self, course_code, course_name, credits, max_students, enrolled_students, instructor):

        self.course_code = course_code
        self.course_name = course_name
        self.credits = credits
        self.max_students = max_students
        self.enrolled_students = enrolled_students
        self.instructor = instructor

    def __str__(self):
        return f"Course Code: {self.course_code}, Course Name: {self.course_name}, Credits: {self.credits}, Max Students: {self.max_students}, Enrolled Students: {self.enrolled_students}, Instructor: {self.instructor}"


    def enroll_student(self):
        if self.enrolled_students < self.max_students:
            self.enrolled_students += 1
            return f"Student enrolled successfully. Total enrolled students: {self.enrolled_students}"
        else:
            return f"Cannot enroll student. Course is full."


    def drop_student(self):
        if self.enrolled_students > self.max_students:
            self.enrolled_students -= 1 
            return f"sorry we have to drop you:"
        else:
            return f"Student enrolled successfully."


    def available_seats(self):
        return self.max_students - self.enrolled_students


    def change_instructor(self, new_instructor):
        self.instructor = new_instructor
        return f"Instructor changed to {self.instructor}"

    def class_roster(self):
        return f"Course Code: {self.course_code}, Course Name: {self.course_name}, Instructor: {self.instructor}, Enrolled Students: {self.enrolled_students}"

    def course_load(self):
        return f"Course Code: {self.course_code}, Course Name: {self.course_name}, Credits: {self.credits}, Enrolled Students: {self.enrolled_students}, Instructor: {self.instructor}"


student1 = Course_Registration_System(course_code="CS101", course_name="Introduction to Computer Science", credits=3, max_students=30, enrolled_students=25, instructor="Dr. Smith")


print(student1)
        






