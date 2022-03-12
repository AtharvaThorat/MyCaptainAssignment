nterms = int(input("Enter the number of terms to print in Fibonacci series: "))
n1 = 0
n2 = 1
count = 0

if nterms <= 0:
    print("Number Invalid, please enter a positive number")
elif nterms == 1:
    print("The Fibonacci sequence of the numbers up to", nterms, ":")
    print(n1)
else:
    print("The Fibonacci sequence of the numbers is:")
    while count < nterms:
        print(n1)
        nth  = n1 + n2

        n1 = n2
        n2 = nth
        count += 1
