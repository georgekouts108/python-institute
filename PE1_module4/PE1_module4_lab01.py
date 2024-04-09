def is_year_leap(year):
#
# Write your code here.
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
        
test_data = [1900, 2000, 2016, 1987]
test_results = [False, True, True, False]
for i in range(len(test_data)):
    yr = test_data[i]
    print(yr,"->",end="")
    result = is_year_leap(yr)
    if result == test_results[i]:
        print("OK")
    else:
        print("Failed")
