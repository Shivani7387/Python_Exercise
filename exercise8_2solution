# -------------------------------------------
# Exercise 02 : Classes and objects -- try creating this in oops world
# -------------------------------------------
 
# Create a class that captures airline tickets. 
# Each ticket lists the departure and arrival cities, a flight number, and a seat assignment. 
# A seat assignment has both a row and a letter for the seat within the row (such as 12F). 

# main method:
# Make two examples of tickets being sold to passengers.
# display tickets booked details 


class My_airline :
    airline_name = 'Gaurav Airline'
    cities = {'Delhi','Pune','Mumbai','Bangalore','Chennai','Hyderabad','Patna','Trivandrum'}
    rows = set(range(1,21))
    section = {'A','B','C','D','E','F'}
    flight_numbers = set(range(564262,564362))
    
    def __init__(self,rcv_fn= None,rcv_dep = None , rcv_arr= None, rcv_sn = None) -> None:
        self.flight_number =  My_airline.flight_numbers.pop()  if rcv_fn is None else rcv_fn
        self.departure = My_airline.cities.pop() if rcv_dep is None else rcv_dep
        self.arrival = My_airline.cities.pop() if rcv_arr is None else rcv_arr
        self.seat_number = str(My_airline.rows.pop()) + My_airline.section.pop() if rcv_sn is None else rcv_sn
        
    def display_details(self):
        print(f"""Your ticket details :
--------------------------------------               
Airline_name : {My_airline.airline_name}
Flight_number : {self.flight_number}
Departure: {self.departure}
Arrival: {self.arrival}
Seat_number: {self.seat_number}
              
              """)   


def main():
   ticket_number1 = My_airline(1111111,'LONDON','USA','XXX1') 
   ticket_number2 = My_airline()
   
   ticket_number1.display_details()
   ticket_number2.display_details()

main()


# var = None
# flight_number =  1  if var else 2   
# print(flight_number)      
