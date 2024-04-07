c0 = int(input("Enter a positive number greater than zero: "))

count = 0

while True:
    count+=1

    if c0 % 2 == 0:
        c0 = c0 // 2

    elif c0 % 2 == 1:
        c0 = 3*c0 + 1

    print(f"c0 = {c0}")

    if c0 != 1:
        continue
    else:
        break

print(f"steps = {count}")

    
