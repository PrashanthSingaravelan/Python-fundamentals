import Module1  # Importing the Module1 so as to include all its features

courses = ['Maths','Physics','Chemistry','Biology','French']
print("Physics is found at : ",Module1.find_index(courses,'Physics'))   
# '<Imported Module name>'.function_name

import Module1 as nm  # if the file name is toolong we can import it as short form
print("Maths is found at : ",nm.find_index(courses,"Maths"))

from Module1 import find_index  # From Module1 import specific functions which are used in Module2
print("Biology is found at : ",find_index(courses,'Biology'))
# Now test_string is not accessible. find_index is only accessible

############
from Module1 import find_index,test_string
print(test_string)
#############

###########
import sys 
#print(sys.path)
###########

######## Importing file from different directory
sys.path.append('F:\Additional Learning\Python skills\Basics Python\Simple logics\ASCII values')

import os
print("Current working directory : ",os.getcwd())

import antigravity
