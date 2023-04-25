# -------------------------------------------
# Exercise 02 : Classes and objects -- try creating this in oops world
# -------------------------------------------
 
# Create a class that captures airline tickets. 
# Each ticket lists the departure and arrival cities, a flight number, and a seat assignment. 
# A seat assignment has both a row and a letter for the seat within the row (such as 12F). 

# main method:
# Make two examples of tickets being sold to passengers.
# display tickets booked details 


class Air_ticket:
   
    
    def __init__(self):
        self.tkt_num = None
        self.psnger_name = None
        self.arrive = None
        self.departure = None
        self.flt_num = None
        self.seat_no = None
     
    def get_vals(self):
        self.tkt_num = input("Ticket number: ")
        self.psnger_name = input("Passenger Name: ")
        self.arrive = input("Arrival: ")
        self.departure =input("Departure: ")
        self.flt_num = input("Flight no: ")
        self.seat_no = input("Seat no.: ")

    

def main():
    #tkt_num,psnger_name,arrive,departure,flt_num,seat_no = input("Ticket number: "),input("Passenger Name: "),input("Arrival: "),\
                                                           #input("Departure: "),input("Flight no: "),input("Seat no.: ")
                                                         
    a = [0,0,0]    #a1 = Air_ticket()
    for i in range(len(a)):
        a[i] = Air_ticket()
        a[i].get_vals()
        print(f"""-------------------------------------------------------------------------------------------------")
                      Ticket No :      {a[i].tkt_num} \n")
                      Seat No   :      {a[i].seat_no}                                    Flight No. :   {a[i].flt_num}\n")
                      Name      :      {a[i].psnger_name}\n")
                     Arrival   :      {a[i].arrive}                                     departure :    {a[i].departure}")
        ---------------------------------------------------------------------------------------------------\n""")


    #a2 = Air_ticket(tkt_num,psnger_name,arrive,departure,flt_num,seat_no)


main()
