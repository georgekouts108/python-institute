def read_int(prompt, min, max):
    #
    # Write your code here.
    #
    while True:
        try:
            number = int(input(prompt))
            if number in range(min, max+1):
                return number
            raise
        except ValueError:
            print("Error: wrong input.")
        except:
            print(f"Error: the value is not within permitted range ({min}..{max})")
    
    


v = read_int("Enter a number from -10 to 10: ", -10, 10)

print("The number is:", v)
