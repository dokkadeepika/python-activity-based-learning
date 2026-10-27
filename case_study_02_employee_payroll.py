##Algorithm
Start.
Read employee name and basic salary.
Calculate HRA as 20% of basic salary.
Calculate DA as 10% of basic salary.
Calculate gross salary.
Calculate deduction as 5% of gross salary.
Calculate net salary.
Display the salary details.
Stop.
##flowchart

         ( START )
             |
       / Read salary details /
             |
       < Invalid values? >
          /        \
        Yes         No
         |           |
   [Print error] [Calculate allowances
         |         and overtime]
        (END)          |
                  [Calculate gross salary]
                         |
                  [Calculate deduction]
                         |
                   [Net = Gross - Deduction]
                         |
                   / Print salary statement /
                         |
                       ( END )

##python code
basic = float(input("Enter basic salary: "))
allowances = float(input("Enter allowances: "))
overtime = float(input("Enter overtime pay: "))
incentives = float(input("Enter incentives: "))

gross = basic + allowances + overtime + incentives

if gross <= 20000:
    deduction = gross * 0.05
else:
    deduction = 20000 * 0.05 + (gross - 20000) * 0.10

net = gross - deduction

print("Gross Salary: Rs.", gross)
print("Deduction: Rs.", deduction)
print("Net Salary: Rs.", net)
##output
Enter employee name: Ravi
Enter basic salary: 20000
Employee Name: Ravi
HRA: 4000.0
DA: 2000.0
Gross Salary: 26000.0
Deduction: 1300.0
Net Salary: 24700.0