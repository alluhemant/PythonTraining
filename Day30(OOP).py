class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.grades = []

    def add_grades(self, grade):
        if grade not in self.grades:
            self.grades.append(grade)
        else:
            return "Not a valid grade"
        print(self.grades)

    def calculate_average(self):
        sum_of_nos = 0
        for i in range(len(self.grades)):
            sum_of_nos += self.grades[i]
            i += 1
        average = sum_of_nos / len(self.grades)
        return f"The average of the student is {average}"

    def display_student_info(self):
        return f"The student name: {self.name}\nThe student age: {self.age}\n{self.calculate_average()}"


student1 = Student("Hemant", 20)
student1.add_grades(90)
student1.add_grades(80)
student1.add_grades(75)

print(student1.display_student_info())
