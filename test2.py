#max
list1=input("enter list:").split(",")
max1=0
for i in range(0,len(list1),1):
    list1[i]=int(list1[i])
print(list1)
for i in range(len(list1)):    
    if max1<list1[i]:
        max1=list1[i]
print(max1)

#reversed

list1=input("enter list:").split(",")
for i in range(0,len(list1),1):
    list1[i]=int(list1[i])
print(list1)    
list1=list1[::-1]
print(list1)

#concaniate list index wise

#list1=input("enter list:").split(",")
list1=["M","na"]
list2=["y","me"]
for i in range(0,len(list1)):
    list1[i]=list1[i]+(list2[i])
print(list1)

#square of each index of list
list1=[1,2,3,4]
for i in range(len(list1)):
    list1[i]=int(list1[i])
for i in range(0,len(list1)):
    list1[i]=list1[i]*list1[i]
print(list1)
        
# list1 = ["Hello ", "take "]
# list2 = ["Dear", "Sir"]
# ['Hello Dear', 'Hello Sir', 'take Dear', 'take Sir']

list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]
list3 = []
for i in range(0,len(list1),1):
    for j in range(0,len(list2),1):
        list3.append(list1[i]+list2[j])
        
print(list3)


#Exercise 5: Iterate both lists simultaneously
#list1 = [10, 20, 30, 40]
#list2 = [100, 200, 300, 400]
#10 400
#20 300
#30 200
#40 100       

list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]

for i in range(len(list1)):
    print(list1[i] ,end=" ")
    print(list2[-(i+1)])

#Exercise 6: Remove empty strings from the list of strings
#list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]
#output : ["Mike", "Emma", "Kelly", "Brad"]

list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]

for l in list1:
    if l == "":
        list1.remove(l)
print(list1)

#Exercise 7: Add new item to list after a specified item
#list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
#output = [10, 20, [300, 400, [5000, 6000, 7000], 500], 30, 40]

list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]

list1[2][2].append(7000)
print(list1)


#Exercise 8: Extend nested list by adding the sublist
#list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
# sub list to add
#sub_list = ["h", "i", "j"]
#['a', 'b', ['c', ['d', 'e', ['f', 'g', 'h', 'i', 'j'], 'k'], 'l'], 'm', 'n']

list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
sub_list = ["h", "i", "j"]
list1[2][2].extend(sub_list)


#Exercise 9: Replace list’s item with new value if found
#list1 = [5, 10, 15, 20, 25, 50, 20]
#output : [5, 10, 15, 200, 25, 50, 20]

list1 = [5, 10, 15, 20, 25, 50, 20]

indx = list1.index(20)
list1[indx]=200

#Exercise 10: Remove all occurrences of a specific item from a list.
