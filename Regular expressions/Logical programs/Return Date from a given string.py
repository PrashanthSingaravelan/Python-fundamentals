import re
string1="My booking is made on 12-04-2019 and the flight number is 564-723-8976. The date of departure is 30-06-2020"
print("The date in the above string is : ",end=" ")

# Instead of the below code
#print(*re.findall(r'\d\d-\d\d-\d\d\d\d',string1))

# To print only the dates
print(*re.findall("\d{2}-\d{2}-\d{4}",string1)) # 12-04-2019 30-06-2020

# To print only the years
print(*re.findall("\d{2}-\d{2}-(\d{4})",string1)) # 2019 2020
# Only the last (\d{4}) => will be more focussed and printed

