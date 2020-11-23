def convert24(str1):                               # Default Conditions
    if str1[-2:] == "AM" and str1[:2] == "12":  # 1) If 12:23:43 AM => 00:23:43 
        return "00" + str1[2:-2]
    elif str1[-2:] == "AM":                     # 2) From Morning 1 to 11 AM => Same as like that
        return str1[:-2]
    elif str1[-2:] == "PM" and str1[:2] == "12": # From noon 1 to night 11 PM => Convert 
        return str1[:-2]
    else:
        return str(int(str1[:2]) + 12) + str1[2:8]

print(convert24("08:65:45 PM"))