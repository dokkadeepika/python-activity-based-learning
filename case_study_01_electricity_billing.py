##Algorithm
1.Start
2.read the number of electricity units consumed
3.Calculate the bill using progressive unit rates.
4.Add the fixed charge.
5.Display the total bill.
6.Stop.
##Flowchart

       ( START )
           |
      / Read units /
           |
      < Units < 0? >
        /       \
      Yes        No
       |          |
 [Print error] [Calculate slab
       |        charges]
      (END)        |
              [Add fixed charge]
                    |
              < Units > 250? >
                /       \
              Yes        No
               |          |
        [Add surcharge]   |
               \         /
                [Calculate total]
                     |
               / Print bill /
                     |
                   ( END )

##Python Code
units = int(input("Enter electricity units: "))

if units < 0:
    print("Invalid units")
else:
    if units <= 100:
        bill = units * 2
    elif units <= 200:
        bill = 100 * 2 + (units - 100) * 3
    else:
        bill = 100 * 2 + 100 * 3 + (units - 200) * 5

    bill += 50  # Fixed charge
    print("Electricity Bill: Rs.", bill)
 ##output
 Enter electricity units: 250
Total Electricity Bill = Rs.800