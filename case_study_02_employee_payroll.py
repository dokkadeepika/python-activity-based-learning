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