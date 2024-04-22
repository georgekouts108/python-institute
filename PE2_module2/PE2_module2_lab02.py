zero = [[1,1,1],[1,0,1],[1,0,1],[1,0,1],[1,1,1]]
one = [[0,0,1],[0,0,1],[0,0,1],[0,0,1],[0,0,1]]
two = [[1,1,1],[0,0,1],[1,1,1],[1,0,0],[1,1,1]]
three = [[1,1,1],[0,0,1],[1,1,1],[0,0,1],[1,1,1]]
four = [[1,0,1],[1,0,1],[1,1,1],[0,0,1],[0,0,1]]
five = [[1,1,1],[1,0,0],[1,1,1],[0,0,1],[1,1,1]]
six = [[1,1,1],[1,0,0],[1,1,1],[1,0,1],[1,1,1]]
seven = [[1,1,1],[0,0,1],[0,0,1],[0,0,1],[0,0,1]]
eight = [[1,1,1],[1,0,1],[1,1,1],[1,0,1],[1,1,1]]
nine = [[1,1,1],[1,0,1],[1,1,1],[0,0,1],[1,1,1]]

numbers = {0:zero, 1:one, 2:two, 3:three, 4:four, 5:five, 6:six, 7:seven, 8:eight, 9:nine}

def display(number):
    rows = []
    for i in str(number):
        rows.append(numbers[int(i)])
   
    for col in range(5):
        row_line = ''
        for row in rows:
            trio = row[col]
            trio_hashes = ''
            for t in trio:
                trio_hashes += '#' if t==1 else ' '
                
            row_line += trio_hashes + " "
        
        print(row_line)
