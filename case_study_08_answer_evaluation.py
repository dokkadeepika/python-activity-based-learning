##alogarithm
1.	Start.
2.	Create a nested list of student marks.
3.	Calculate each student's total and average.
4.	Calculate the average for each subject.
5.	Track the student with the highest total.
6.	Print student and subject statistics.
7.	End.
##flowchart
          ( START )
              |
    / Read correct and student answers /
              |
       < Input is valid? >
          /        \
        No          Yes
         |           |
   [Print error] [Normalize answers]
         |           |
       (END)   < Answers match? >
                  /        \
                Yes         No
                 |           |
            [Award marks] [Award zero]
                 \           /
                / Print result /
                       |
                    ( END )
##python code
key = input("Enter answer key: ").upper()
answers = input("Enter student answers: ").upper()

if len(key) != len(answers):
    print("Answer count does not match")
else:
    correct = 0
    wrong = 0
    unanswered = 0

    for i in range(len(key)):
        if answers[i] == "-":
            unanswered += 1
        elif answers[i] == key[i]:
            correct += 1
        else:
            wrong += 1

    score = correct * 1 - wrong * 0.25

    print("Correct Answers:", correct)
    print("Wrong Answers:", wrong)
    print("Unanswered:", unanswered)
    print("Final Score:", score)
##output
Enter answer key: ABCD
Enter student answers: AB-C
Correct Answers: 2
Wrong Answers: 1
Unanswered: 1
Final Score: 1.75