# Exercise 1: Print First 10 natural numbers using while loop
num=int(input("enter the number: "))
f0=0
f1=1
i=0
for i in range(num):
     f2=f0+f1
     f0=f1
     f1=f2
     print(f0)

