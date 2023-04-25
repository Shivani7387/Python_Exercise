# #Exercise 1: Print First 10 natural numbers using while loop
a=1
while (a<=10):
    print(a)
    a=a+1
    

# #Exercise 2: Print the following pattern
num=int(input("enter number:"))
for i in range(num+1):
     print("\n")
     for j in range(1,i+1):
       print(j, end=" ")
      
       
#  #Exercise 3: Calculate the sum of all numbers from 1 to a given number      
num=int(input("enter number:"))
sum=0
for i in range(num+1):
    sum=sum+i
    
print("sum=:",sum)
#OR
a=1
while(a<num+1):
    sum=sum+a
    a=a+1
print("sum:",sum)


# #Exercise 4: Write a program to print multiplication table of a given number
a=1
while(a<=10):
    mult=num*a
    print(f"{num}*{a}:",mult)
    a=a+1
    
# #Exercise 5: Display numbers from a list using loop
numbers = [12, 75, 150, 180, 145, 525, 50]
for i in range(len(numbers)):
    print(numbers[i] , end=" ")


# #Exercise 6: Count the total number of digits in a number
num=int(input("enter number: "))
co=0
while(num>=1):
    num=num/10
    co=co+1
print(co) 

# Exercise 7: Print the following pattern
# 5 4 3 2 1 
# 4 3 2 1 
# 3 2 1 
# 2 1 
# 1
num=int(input("enter number:"))
for i in range(num+1):
    print("\n")
    for j in reversed(range(i+1,num+1)):
       print(j, end=" ") 
      

# #Exercise 8: Print list in reverse order using a loop
list1 = [10, 20, 30, 40, 50]
for i in reversed(range(len(list1))):
    print(list1[i])


# #Exercise 9: Display numbers from -10 to -1 using for loop
for i in range(-10,0):
    print(i)
    
    
# #Exercise 10: Use else block to display a message “Done” after successful execution of for loop
for i in range(-10,0):
    if(True):
        print(i)
else:
    print("DONE")
    
    
# #Exercise 11: Write a program to display all prime numbers within a range
num2=int(input("enter number:"))
for j in range(num2+1):
    if j>1:
        for i in range(2,j):
            if j%i==0:
                break
        else:
            print(j)
            

# #Exercise 12: Display Fibonacci series up to 10 terms
fib1=0
fib2=1
i=0
num4,n=int(input("enter number:")),int(input("enter where to stop:"))
for i in range(num4+1):
    fibn=fib1+fib2
    print(fib1)
    fib1=fib2
    fib2=fibn
    if fib1>n:
        break


# #Exercise 13: Find the factorial of a given number








 #Exercise 14: Reverse a given integer number    
a=0
m=0
num=int(input("enter number:"))
while(num>=1):
    m=num%10
    #print(m, end="")
    num=num//10
    a=(a*10)+m
print(a,end="")



#Exercise 15: Use a loop to display elements from a given list present at odd index positions
list=[10, 20, 30, 40, 50, 60, 70, 80, 90, 10]
for i in range(len(list)):
    if i%2!=0:
        print(list[i] , end=" ")
    
    

#Exercise 16: Calculate the cube of all numbers from 1 to a given number
num=int(input("enter number:"))
a=1
while(a<=num):
    mult=a**3
    print(mult)
    a=a+1



#Exercise 17: Find the sum of the series upto n terms
num=int(input("enter series num:"))
a=int(input("enter number:"))



#Exercise 18: Print the following pattern
num=int(input("enter number:"))
a=num//2
#b=1
for i in range(1,num+1):
     print("\n")
     for k in range(num-i):
        print("_", end=" ")
     for j in range(0,(i*2)-1):
        print("*", end=" ")
