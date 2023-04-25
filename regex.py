import re

a=re.search("^[0-9]*[_][a-z].*[@].*","2009_rocking_person@yahoo.com")
                        # 2009_rocking_person@yahoo.com
                        # GodFather2022@yahoo.com
                        # Brocklesner_89_WWE@yahoo.com
                        # TheRock_WWE@yahoo.com
                        # JohnCena_WWE@yahoo.com
                        # Undertaker_Roman_reigns@outlook.com
                        # 6789764666@rediffmail.com
                        # Kane#6789@gmail.com''')
                    
print(a)
#print(a.group(0))
# print(a.group(1))
# print(a.group(2))
# print(a.group(3))