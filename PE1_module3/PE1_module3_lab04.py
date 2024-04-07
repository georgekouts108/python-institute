year = int(input("Enter a year: "))

#
# Write your code here.
#
if year < 1582:
    print("Not within the Gregorian calendar period")
else:
    if year % 4 != 0:
        print("Common year")
    else:
        if year % 100 == 0:
            if year % 400 != 0:
                print("Common year")
            else:
                print("Leap year")
        else:
            print("Leap year")
