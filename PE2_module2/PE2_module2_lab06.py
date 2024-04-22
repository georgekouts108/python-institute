def digit_of_life(birthday):
    dol = 0
    
    bday = str(birthday)
    while True:
        total = 0
        for b in bday:
            total += int(b)
        
        if total < 10:
            dol = total
            break
        else:
            bday = str(total)
        
    return dol
