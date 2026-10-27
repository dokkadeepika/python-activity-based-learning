##Algorithm
1.Start.
2.Initialize the account balance and transaction counters.
3.Display the transaction menu.
4.Read the transaction type: deposit, withdrawal or quit.
5.If the transaction is a deposit, read the amount and add it to the balance if valid.
6.If the transaction is a withdrawal, check the amount and available balance.
7.Reject invalid transactions and display the appropriate message.
8.Repeat the process until the user selects quit.
9.Display the number of successful deposits, withdrawals and the final balance.
10.Stop.
##flowchart
          ( START )
              |
       / Read initial balance /
              |
       / Select transaction /
              |
       < Valid transaction? >
          /        \
        No          Yes
         |           |
   [Print error] < Withdraw? >
         |          /      \
       (END)      Yes       No
                   |         |
          < Sufficient   < Deposit? >
             balance? >    /     \
             /     \     Yes      No
           No      Yes    |        |
            |       | [Add amount] [Show balance]
      [Reject] [Subtract amount]     |
            \       /                |
             [Update balance]         |
                    \                /
                    / Print balance /
                           |
                        ( END )
##python code
balance = float(input("Enter opening balance: "))
n = int(input("Enter number of transactions: "))

for i in range(n):
    print("1. Deposit  2. Withdraw")
    choice = int(input("Enter choice: "))
    amount = float(input("Enter amount: "))

    if amount <= 0:
        print("Invalid amount")
    elif choice == 1:
        balance += amount
        print("Deposit successful")
    elif choice == 2:
        if amount <= balance:
            balance -= amount
            print("Withdrawal successful")
        else:
            print("Insufficient balance")
    else:
        print("Invalid choice")

    print("Current balance: Rs.", balance)

print("Final balance: Rs.", balance)
##output
Enter opening balance: 1000
Enter number of transactions: 2
1. Deposit  2. Withdraw
Enter choice: 1
Enter amount: 500
Deposit successful
Current balance: Rs. 1500.0
1. Deposit  2. Withdraw
Enter choice: 2
Enter amount: 200
Withdrawal successful
Current balance: Rs. 1300.0
Final balance: Rs. 1300.0