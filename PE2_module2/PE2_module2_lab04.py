def is_palindrome(string):

    if string == '':
        return False

    edited = "".join(string.split(' '))
    
    lo = 0
    hi = len(edited) - 1

    while lo < hi:
        if edited[lo].lower() != edited[hi].lower():
            return False
        lo+=1
        hi-=1
        
    return True

text = input("Enter some text: ")
palindrome = is_palindrome(text)

print(f"It's {'not ' if not palindrome else ''}a palindrome")
