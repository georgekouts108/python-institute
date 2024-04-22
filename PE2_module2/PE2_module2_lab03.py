uppercases = []
lowercases = []
for u in range(65,91):
    uppercases.append(chr(u))
    lowercases.append(chr(u+32))

def shift(char, amount):
    result = ''
    if ord(char) in range(65,91):
        return uppercases[ (uppercases.index(char) + amount ) % 26]
        
    elif ord(char) in range(97,123):
        return lowercases[ (lowercases.index(char) + amount ) % 26]
        
    return char

def encrypt(message, shift_val):
    result = ''
    for m in message:
        result += shift(m, shift_val)
    
    return result
    

message = input("Enter a message you want to encrypt: ")
shift_val = 0
while True:
    try:
        shift_val = int(input("Enter a shift value from 1 to 25 (inclusive): "))
        if shift_val in range(1,26):
            break
        else:
            raise Exception()
    except:
        print("An error occurred.")

encryption = encrypt(message, shift_val)
print(f"Encrypted message: {encryption}")

