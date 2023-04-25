# program where we are using os module along with file handling
import os 

current_file_abs_path = __file__ # gives absolute path of the file 
current_directory = os.getcwd() # gives current working directory path 
target_folder_path = os.path.join(current_directory,'output') # creates path from strings

if 'output' not in os.listdir(current_directory): # gets all files folders in list
     os.mkdir(target_folder_path) # creates a folder

target_path = os.path.join(target_folder_path,'my_first_file_output.txt')

# output_file= open('C:\\Users\\acer\\Desktop\\HPCSA_python\\output\\my_first_file_output.txt','w+')
output_file= open(target_path,'w+') # we use the variable instead of harcoded value
for input_line in open('my_first_file.txt'):
    output_file.write('HPCSA'+input_line)

output_file.seek(0)    
print(output_file.read())    

print(__file__)