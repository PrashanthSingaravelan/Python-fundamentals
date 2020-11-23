from datetime import date
today=date.today()
print("Today : ",today)

# dd/mm/yy
print("dd/mm/yy : ",today.strftime("%d/%m/%y"))

#  Date / Textual month(full form) / year
print("Date/Textual month (full form) /year : ",today.strftime("%d/%B/%y"))

#  Date / Textual month(short form) / year
print("Date / Textual month (short form) / year : ",today.strftime("%d/%b/%y"))

