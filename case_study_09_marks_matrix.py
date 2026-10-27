##alogarithm
1.Start.
2.Create a nested list containing student marks in different subjects.
3.Calculate each student's total marks.
4.Calculate each student's average marks.
5.Calculate the average marks for each subject.
6.Identify the student with the highest total marks.
7.Display each student's total and average, subject averages and the top performer.
8.Stop.

##flowchart
          ( START )
              |
       / Read student marks /
              |
       < Marks are valid? >
          /        \
        No          Yes
         |           |
   [Print error] [Calculate each student's
         |          total and average]
       (END)             |
                   [Find highest mark]
                         |
                    [Find lowest mark]
                         |
                   / Print analysis /
                         |
                      ( END )
##python code
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
##output
Enter number of students: 2
Enter number of subjects: 2
Student 1
Enter marks: 80
Enter marks: 90
Student 2
Enter marks: 70
Enter marks: 60
Student 1 Average: 85.0
Student 2 Average: 65.0
Subject 1 Average: 75.0
Subject 2 Average: 75.0