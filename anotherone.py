########################################################################
######################## Practice problem1 #############################

contact={ "shivani":15498584,
          "sru":546589465,
          "nits":1354654}

def con_add(contact):
    n,c = input("eneter the name and the contact number").split(",")
    contact[n]=c
    print(contact)
    
def con_del():
    n = input("enter the name to delete the contact")
    del contact[n]
    print(contact)
    
def con_search():
    n = input("eneter the name to search the contact")
    for i in list(contact.keys()):
        if i==n:
            print(contact[i])
    
def con_backup():
    backup = {}
    for i in contact.keys():
        backup[i]=contact[i]
    print("Backedup successfully..")
    

def menu():
    print("1.ADD \n 2.DELETE \n 3.SEARCH \n 4.BACKUP \n 5.EXIT")
    inp = int(input("eneter your choice"))
    return inp
    
ch="y"
while(ch=="y"):
    inp = menu()
    if inp==1:
        con_add(contact)
        ch = input("do you want to contiue (Y/N) :").lower()
    
    elif inp==2:
        con_del()
        ch = input("do you want to contiue (Y/N) :").lower()

    elif inp==3:
        con_search()
        ch = input("do you want to contiue (Y/N) :").lower()
        
    elif inp==4:
        con_backup()
        ch = input("do you want to contiue (Y/N) :").lower()

    else:
        break
        
    
    
    