# ----- Inheritance exercise ----
# 1. Define  
#   Person (superclass) that has name , place_of_residence , display_attributes()
#   Sister (subclass of Person)  that has additionally exam_subjects , display_attributes()
#   Uncle (subclass of Persom)  that has additionally business , display_attributes()

# main method:
# create a sister class object and display its attributes 
# create a Uncle class object and display its attributes 
class person:
      def __init__(self,name,age,address,height):
         
          print(name," ",age," ",address," ",height)
object=person("vikas",23,"delhi",5.5)

# # print(object.viku)  
# print(person.viku)
# print(object.__doc__)
