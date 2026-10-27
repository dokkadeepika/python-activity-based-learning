##algorithm
1.Start.
2.Read the number of examinations, n.
3.Read and store marks in a list.
4.If n = 0, display “No marks entered”.
5.Otherwise, display marks and compare consecutive marks.
6.Display improvement, decline, or unchanged marks.
7.Calculate and display average marks.
8.Classify performance as Excellent, Good, or Needs Improvement.
9.Stop.
##flowchart
          ( START )
              |
     / Read number of examinations n /
              |
        < n == 0? >
          /       \
        Yes        No
         |          |
 [Print "No marks   |
   entered"]       |
         |     / Input marks /
       (END)       |
              [Store marks in list]
                     |
              < More marks to enter? >
                  /       \
                Yes        No
                 |          |
             / Read mark /  |
                 |     [Display marks]
                 |          |
                 +----> [Compare consecutive
                         examination marks]
                              |
                       < Change in marks? >
                       /       |       \
                   Positive  Negative  Zero
                      |         |       |
                [Print       [Print   [Print
                improved]   declined] unchanged]
                       \       |       /
                        [Calculate average]
                               |
                       [Display average]
                               |
                       < Average >= 75? >
                         /          \
                       Yes           No
                        |             |
                [Excellent]   < Average >= 50? >
                                /          \
                              Yes           No
                               |             |
                            [Good]    [Needs Improvement]
                               \             /
                             / Print performance /
                                      |
                                   ( END )
##python code
n = int(input("Enter number of examinations: "))
marks = []

for i in range(n):
    mark = float(input("Enter marks: "))
    marks.append(mark)

if n == 0:
    print("No marks entered")
else:
    print("Marks:", marks)

    for i in range(1, n):
        change = marks[i] - marks[i - 1]

        if change > 0:
            print("Improved by:", change)
        elif change < 0:
            print("Declined by:", abs(change))
        else:
            print("Marks unchanged")

    average = sum(marks) / n
    print("Average Marks:", round(average, 2))

    if average >= 75:
        print("Performance: Excellent")
    elif average >= 50:
        print("Performance: Good")
    else:
        print("Performance: Needs Improvement")
##output
Enter number of examinations: 3
Enter marks: 60
Enter marks: 75
Enter marks: 70
Marks: [60.0, 75.0, 70.0]
Improved by: 15.0
Declined by: 5.0
Average Marks: 68.33
Performance: Good