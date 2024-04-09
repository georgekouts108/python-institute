def is_year_leap(year):
#
# Your code from LAB 4.3.1.6.
#
    leap = False
    
    if year % 4 != 0:
        leap = False
    else:
        if year % 100 == 0:
            if year % 400 != 0:
                leap = False
            else:
                leap = True
        else:
            leap = True
    
    return leap

def days_in_month(year, month):
#
# Write your new code here.
#
    if month == 2:
        return 29 if is_year_leap(year) else 28
    
    return 31 if month in [1, 3, 5, 7, 8, 10, 12] else 30
    
        
def day_of_year(year, month, day):
#
# Write your new code here.
#
    if (len(str(year)) != 4) or (month not in range(1,13)) or (day not in range(1,32)):
        return None

    if (month==2 and day==29 and not is_leap_year(year)):
        return None

    month_names = {1:'Jan',2:'Feb',3:'Mar',4:'Apr',5:'May',6:'Jun',
                   7:'Jul',8:'Aug',9:'Sep',10:'Oct',11:'Nov',12:'Dec'}

    return month_names[month] + " " + str(day) + ", " + str(year)
    

print(day_of_year(2000, 12, 31))
