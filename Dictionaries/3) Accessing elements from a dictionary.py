# In order to access the items of a dictionary refer to its key name.
# Key can be used inside square brackets.
# There is also a method called get() that will also help in acessing the element from a dictionary.

dict1=dict({"Name":"Prashanth","Age":"18","DOB":"24th April 2001"})
print(dict1)  # {'Name': 'Prashanth', 'Age': '18', 'DOB': '24th April 2001'}

# Accessing the elements using keys
print(dict1["Age"]) # 18

# Accessing using get()
print(dict1.get("DOB")) #24th April 2001

dict2=dict([(1, 'eggs'),(2, 'omelete'),(3, 'Bread'),('Breakfast', 'Dosa')] )
print(dict2)

