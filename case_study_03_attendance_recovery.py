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