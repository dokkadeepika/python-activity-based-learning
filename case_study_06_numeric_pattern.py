##alogarithm
1.Start.
2.Read diamond size n.
3.If n <= 0, display an error message.
4.Print the upper half of the diamond using loops.
5.Print the lower half in reverse order.
6.Stop.
##flowchart
          ( START )
              |
       / Read diamond size n /
              |
          < n <= 0? >
           /       \
         Yes        No
          |          |
 [Print positive    |
     number]        |
          |     [Set i = 1]
        (END)       |
              < i <= n? >
                /      \
              Yes       No
               |         |
       [Print n-i spaces]|
               |         |
       [Print numbers    |
        1 to i]          |
               |         |
       [Print numbers    |
        i-1 down to 1]   |
               |         |
         [Print newline] |
               |         |
           [i = i + 1]   |
               |         |
               +----> Repeat
                         |
                  [Set i = n - 1]
                         |
                    < i >= 1? >
                     /       \
                   Yes        No
                    |           |
            [Print n-i spaces] |
                    |           |
            [Print numbers     |
             1 to i]           |
                    |           |
            [Print numbers     |
             i-1 down to 1]    |
                    |           |
              [Print newline]  |
                    |           |
                [i = i - 1]    |
                    |           |
                    +----> Repeat
                                |
                              ( END )
##python code
n = int(input("Enter diamond size: "))

if n <= 0:
    print("Enter a positive number")
else:
    for i in range(1, n + 1):
        print(" " * (n - i), end="")

        for j in range(1, i + 1):
            print(j, end="")

        for j in range(i - 1, 0, -1):
            print(j, end="")

        print()

    for i in range(n - 1, 0, -1):
        print(" " * (n - i), end="")

        for j in range(1, i + 1):
            print(j, end="")

        for j in range(i - 1, 0, -1):
            print(j, end="")

        print()
##output
Enter diamond size: 3
  1
 121
12321
 121
  1      