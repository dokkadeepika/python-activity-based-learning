students = int(input("Enter number of students: "))
subjects = int(input("Enter number of subjects: "))

if students <= 0 or subjects <= 0:
    print("Invalid dimensions")
else:
    marks = []

    for i in range(students):
        row = []
        print("Student", i + 1)

        for j in range(subjects):
            mark = float(input("Enter marks: "))
            row.append(mark)

        marks.append(row)

    for i in range(students):
        average = sum(marks[i]) / subjects
        print("Student", i + 1, "Average:", round(average, 2))

    for j in range(subjects):
        total = 0

        for i in range(students):
            total += marks[i][j]

        print("Subject", j + 1, "Average:", round(total / students, 2))