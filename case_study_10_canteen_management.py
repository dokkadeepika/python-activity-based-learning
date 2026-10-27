##alogarithm
1.	Start.
2.	Store daily prepared meals, served meals, and leftovers.
3.	For each day, validate that values are non-negative and served plus leftovers does not exceed prepared.
4.	Calculate wastage percentage.
5.	Compare percentage with the 10% threshold.
6.	Print each day's report and the days exceeding the limit.
7.	End.
##flowchart
          ( START )
              |
    / Read food prepared and consumed /
              |
       < Input valid and consumed
             <= prepared? >
          /        \
        No          Yes
         |           |
   [Print error] [Calculate food wasted]
         |           |
       (END)   [Calculate waste %]
                     |
               < Waste % >= 20%? >
                  /        \
                Yes         No
                 |           |
           [High waste] [Acceptable waste]
                 \           /
                 / Print report /
                       |
                    ( END )
##python code
items = ["Idli", "Dosa", "Biryani"]
prices = [30, 50, 120]
stock = [20, 15, 10]

total_sales = 0

print("Menu:")
for i in range(len(items)):
    print(i + 1, items[i], "- Rs.", prices[i],
          "Stock:", stock[i])

n = int(input("Enter number of orders: "))

for i in range(n):
    choice = int(input("Enter item number: "))
    quantity = int(input("Enter quantity: "))

    if choice < 1 or choice > len(items):
        print("Invalid item")
    elif quantity <= 0:
        print("Invalid quantity")
    elif quantity > stock[choice - 1]:
        print("Insufficient stock")
    else:
        index = choice - 1
        bill = prices[index] * quantity
        stock[index] -= quantity
        total_sales += bill

        print("Item:", items[index])
        print("Order bill: Rs.", bill)
        print("Remaining stock:", stock[index])

print("Total sales: Rs.", total_sales)
print("Final stock:", stock)
##output
Menu:
1 Idli - Rs. 30 Stock: 20
2 Dosa - Rs. 50 Stock: 15
3 Biryani - Rs. 120 Stock: 10
Enter number of orders: 2
Enter item number: 1
Enter quantity: 2
Item: Idli
Order bill: Rs. 60
Remaining stock: 18
Enter item number: 3
Enter quantity: 1
Item: Biryani
Order bill: Rs. 120
Remaining stock: 9
Total sales: Rs. 180
Final stock: [18, 15, 9]