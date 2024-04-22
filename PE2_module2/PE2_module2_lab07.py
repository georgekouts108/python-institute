def foo(word, charset):
    res = 'Yes'
    wordlist = list(word)
    c_index = 0
    
    for char in wordlist:
        if charset[c_index:].find(char) != -1:
            c_index = charset.find(char)+1
        else:
            res = "No"
            break
    
    return res
    
print(foo('donor','Nabucodonosor'))
print(foo('donut','Nabucodonosor'))
