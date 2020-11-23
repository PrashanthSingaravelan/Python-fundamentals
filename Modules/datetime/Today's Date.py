from datetime import datetime
now=datetime.now()  # Current Date and Time

today = datetime.today()
print("Today's date:", today)

# Use strftime() to create a string representing date in different format

a1=now.strftime("%d/%m/%Y, %H:%M:%S")
print("date and time:",a1)