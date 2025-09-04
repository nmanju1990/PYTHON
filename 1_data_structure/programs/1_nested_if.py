# Program to find the 3rd largest (smallest) among three numbers using nested if

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a < b:
    if a < c:
        smallest_no = a
        print("1.first test case")
        
    else:
        smallest_no = c
        print("2. 2nd test case")
else:
    if b < c:
        smallest_no = b
        print("3. 3rd test case")
    else:
        smallest_no = c
        print("4. 4th Test case")

print("The 3rd smallest number is:", smallest_no)

''' 
Test case for the above code: 
---------------------------------------------------------------
Test Case 1 (First branch)
--------------------------- 
Input values: a = 5, b = 10, c = 20

English wording: Since a is smaller than both b and c, the program will pick a as the 3rd largest (smallest) number.

Expected output:

first
The  (smallest) number is: 5

Test Case 2 (Second branch)

Input values: a = 15, b = 20, c = 10

English wording: Here a is smaller than b but not smaller than c. So the program will pick c as the 3rd largest (smallest) number.

Expected output:

2nd test case
The 3rd largest (smallest) number is: 10

Test Case 3 (Third branch)

Input values: a = 20, b = 5, c = 30

English wording: In this case a is not smaller than b, but b is smaller than c. So the program will pick b as the 3rd largest (smallest) number.

Expected output:

3rd test case
The 3rd largest (smallest) number is: 5

Test Case 4 (Fourth branch)

Input values: a = 50, b = 40, c = 10

English wording: Here a is not smaller than b, and b is also not smaller than c. So the program will pick c as the 3rd largest (smallest) number.

Expected output:

4th Test case
The 3rd largest (smallest) number is: 10

''' 