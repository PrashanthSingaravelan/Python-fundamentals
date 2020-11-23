# Path specification
import os

# 1) To get working directory as a string value
#print(os.getcwd()) # Previous Directory => F:\Python skills\Python Sample programs\List

# 2) To change the directory
#P print(os.chdir('F:\Python skills\Python Sample programs\File handling'))
#P print(os.getcwd())  # Current Directory => F:\Python skills\Python Sample programs\File handling

# 3) To create a new folder
#os.makedirs("F:\Prashanth\Working\Good")

# 4) Absolute path of the arguments
#P print(os.path.abspath('.') #  F:\Python skills\Python Sample programs\File handling>

# 5) Returns True/False 
print(os.path.isabs("F:"))

# 6)

# 7) Base and Directory name
print(os.path.basename("F:\Python skills\Python Sample programs\File handling\From basics"))  # From basics
print(os.path.dirname("F:\Python skills\Python Sample programs\File handling\From basics"))  # F:\Python skills\Python Sample programs\File handling
 # Using split()
a="F:\Python skills\Python Sample programs\File handling"
print(os.path.split(a))  # ('F:\\Python skills\\Python Sample programs', 'File handling')