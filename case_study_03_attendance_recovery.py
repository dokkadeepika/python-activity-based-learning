##algarithm
1.Start.
2.Read the total number of classes and classes attended.
3.Calculate the current attendance percentage.
4.Check whether the attendance meets the required percentage.
5.If attendance is sufficient, display that the student is eligible.
Otherwise, calculate the number of additional classes required to reach the target attendance.
6.Display the attendance percentage and required additional classes.
7.Stop.
##flowchart
          ( START )
              |
    / Read attended and total classes /
              |
       < Invalid input? >
          /        \
        Yes         No
         |           |
   [Print error] [Calculate attendance %]
         |           |
       (END)   < Attendance >= 75%? >
                    /       \
                  Yes        No
                   |          |
            [Eligible] [Calculate extra classes
                   |     needed to reach 75%]
                   \          /
                   / Print result /
                         |
                      ( END )
##python code
attended = int(input("Enter classes attended: "))
total = int(input("Enter total classes: "))
target = float(input("Enter target attendance percentage: "))

if total <= 0 or attended < 0 or attended > total:
    print("Invalid attendance details")
elif target <= 0 or target > 100:
    print("Invalid target percentage")
else:
    current = attended / total * 100
    print("Current Attendance:", round(current, 2), "%")

    if current >= target:
        print("Target already achieved")
    else:
        required = 0
        while (attended + required) / (total + required) * 100 < target:
            required += 1

        print("Additional classes required:", required)
##output
Enter classes attended: 40
Enter total classes: 50
Enter target attendance percentage: 75
Current Attendance: 80.0 %
Target already achieved