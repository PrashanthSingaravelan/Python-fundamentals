# string.count(substring , start_index, end_index)
# Indexes are optional
# Return Type => int
# Gives 0 if the particular string is not found. But doesn't raises an error

string1="Hi hello How are you? hello Hw are they"
print(string1.count("Dad"))

print(string1.count("hello",0,9)) # Searches only from 0 to 9
