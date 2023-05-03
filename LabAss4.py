#  Reverse a list in Python
# Solution -----------

list1 = []
list1 = input("enter the menbers of the list :").split(",")
print("Reversed List : ",list(reversed(list1)))
# --------------------------------------------------------------------

#  Concatenate two lists index-wise.
# Solution -----------

list1 = input("eneter the list1 :").split(",")
list2 = input("enter the list2 :").split(",")
list3 = list1 + list2
print("concatinating list1 and list2 : ", list3)
#-----------------------------------------------------------------------------

#  Write a Python program to multiply all the items in a list.
# Solution -------------------
list1 = input("Enter the members of the list :").split(",")
mul =1
for i in list1:
    mul = mul * int(i)
print("Multiplication of the items of the list :",mul)
#-------------------------------------------------------------------------------

#  Write a Python program to get the smallest number from a list
# Solution ---------------

list1 = input("Enter the list items :").split(",")
print("smallest number in List :",min(list1))
