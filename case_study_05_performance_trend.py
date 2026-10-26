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