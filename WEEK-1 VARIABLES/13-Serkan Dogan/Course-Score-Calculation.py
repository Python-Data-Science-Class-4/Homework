# Assignment 2.2
# Course Score Calculation

# Student's details
name = input("Enter student's name: ")
surname = input("Enter student's surname: ")
user_name=name+surname
student_number = input("Enter student's number: ")
print("Name of Student; ",name,surname+"\nUser name; ",user_name+"\nStudent number; ",student_number)

# Courses
for i in range(1, 5):
    # Course names and grades for the student
    course_name = input(f"Enter course {i} name: ")
    visa_grade = float(input(f"Enter {course_name} visa grade: "))
    final_grade = float(input(f"Enter {course_name} final grade: "))
    
    # Calculate averages of each course
    average = (0.4 * visa_grade) + (0.6 * final_grade)
    
    # Print course name and grades with averages
    print(course_name, visa_grade,final_grade,"Average;",average)
    
    # Print the result for the course
    if average >= 50:
        print(f"{course_name}: PASSED")
    else:
        print(f"{course_name}: FAILED")