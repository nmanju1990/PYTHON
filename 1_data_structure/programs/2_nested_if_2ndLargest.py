# Program to find the 2nd largest among three numbers using nested if

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a > b:
    if a > c:
        # a is the largest, so 2nd largest is max(b, c)
        if b > c:
            second = b
        else:
            second = c
    else:
        # c is largest, so a is 2nd largest
        second = a
else:
    if b > c:
        # b is largest, so 2nd largest is max(a, c)
        if a > c:
            second = a
        else:
            second = c
    else:
        # c is largest, so b is 2nd largest
        second = b

print("The second largest number is:", second)
