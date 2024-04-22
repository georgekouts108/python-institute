def check_sudoku(grid):
    rows = grid.split()
    
    nine_nums = [str(n) for n in range(1,10)]
    
    ## check each row
    for row in rows:
        if sorted(list(row)) != nine_nums:
            return "No"
    
    ## check each column
    for col in range(9):
        if sorted([ str(row[col]) for row in rows]) != nine_nums:
            return "No"
            
    ## check each square
    squares = []
    r = 0
    while r <= 6:
        square_count = 0
        while square_count < 3:
            next_square = ''
            for row in rows[r:r+3]:
                next_square += row[(square_count * 3) : (square_count * 3)+3]
            squares.append(next_square)
            square_count+=1
        r += 3
    
    for squ in squares:
        if sorted(list(squ)) != nine_nums:
            return "No"
    
    return "Yes"

puzzle1 = '''
295743861
431865927
876192543
387459216
612387495
549216738
763524189
928671354
154938672
'''
puzzle2 = '''
195743862
431865927
876192543
387459216
612387495
549216738
763524189
928671354
254938671
'''
print(check_sudoku(puzzle1))
print(check_sudoku(puzzle2))
