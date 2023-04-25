# ----- Inheritance exercise ----
# 1. Define  
#   Person (superclass) that has name , place_of_residence , display_attributes()
#   Sister (subclass of Person)  that has additionally exam_subjects , display_attributes()
#   Uncle (subclass of Persom)  that has additionally business , display_attributes()

# main method:
# create a sister class object and display its attributes 
# create a Uncle class object and display its attributes 


class Person:
    def __init__(self,name,residence) -> None:
        self.name=name
        self.residence=residence
    
    def display_attr(self):
        print("Person Name : ",self.name)
        print("Residence : ",self.residence)
        

class Sister(Person):
    def __init__(self,name,residence,subs) -> None:
        super().__init__(name,residence)
        self.exam_subs=[]
        self.exam_subs.append(subs)
        
    def display_attr(self):
        super().display_attr()
        print("Exam Subjects : " ,self.exam_subs)
    
class Uncle(Person):
    def __init__(self,name,residence,business) -> None:
        super().__init__(name,residence)
        self.business = business
        
    def display_attr(self):
        super().display_attr()
        print("Business : ",self.business)
        #Sister.display_attr()


def main():
    
    u=Uncle("Vikas","Delhi","XYZ")
    s=Sister("payal","Pune",["python","Java"])
    u.display_attr()
    s.display_attr()

main()
