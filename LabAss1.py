# Lab Assignments:
# Q.1. Using for loop, write and run a Python program for this algorithm.
# Here is an algorithm to print out n! (n factorial) from 0! to 10! :
# 1. Set f = 1
# 2. Set n = 0
# 3. Repeat the following 10 times:
# a. Output n, "! = ", f
# b. Add 1 to n
# c. Multiply f by n

f = 1
i = 1
n=int(input("enter the number to calculate factorial :"))
for i in range(1,n+1):
    f = f * i
    print(f"Factorial of {i} = {f} \n")


# Q.2. Modify the program above using a while loop so it prints out all of the factorial values that are
# less than 2 billion. (You should be able to do this without looking at the output of the previous
# exercise.)
n=2000
while(i<n):
    f = f*i
    i = i + 1
    print(f"Factorial of {i} = {f} \n")
