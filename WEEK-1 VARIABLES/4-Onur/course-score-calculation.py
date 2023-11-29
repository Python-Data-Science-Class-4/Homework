class Lesson:
    def __init__(self, name, midterm, final):
        self.name = name
        self.midterm = float(midterm)
        self.final = float(final)
    
    def calculate(self):
        result = self.midterm*(40/100) + self.final*(60/100)
        if result < 50:
            return "FAILED"
        else:
            return "PASSED"

#inputs from the user
name = input("Please write your name")
surname = input("Please write your surname")
student_number = input("Please write your student number")
lesson_count = int(input("How many lessons do you like to calculate?"))

lesson = 1
lessons = []

while  lesson <= lesson_count:
    temp = input(f"Please write your {lesson}. lesson with grades. Example: Math,80,70").split(",")
    if len(temp) != 3:
        print("Please write the lesson in correct order")
        continue
    lessons.append(Lesson(temp[0],temp[1],temp[2]))
    lesson += 1

print(f"Student {name} {surname} with student id: {student_number}")
for lesson in lessons:
    print(f"Lesson: {lesson.name} // RESULT: {lesson.calculate()} -- Grades: {lesson.midterm} - {lesson.final}")
