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