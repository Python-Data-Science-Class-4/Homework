while True:
    name=input("Enter student name: ")
    surname=input("Enter student surname: ")
    courses = []
    for i in range(4):
        course=[]
        course_name = input("Enter course name: ")
        visa = input("Enter visa: ")
        final = input("Enter final: ")
        course.append(course_name)
        course.append(visa)
        course.append(final)
        print(course)
        courses.append(course)

    for i in courses:
        if (int(i[1])*0.4 + int(i[2])*0.6) < 50:
            print(f"{name} {surname} FAILED from {i[0]}")
        else: 
            print(f"{name} {surname} PASSED from {i[0]}")

    break
