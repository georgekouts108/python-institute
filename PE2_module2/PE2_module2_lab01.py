def mysplit(strng):
    #
    # put your code here
    #
    if strng.strip()=='':
        return []
    
    words = []
    index = 0
    while index < len(strng):
        if strng[index] != ' ':
            next_word=''
            if strng.find(' ', index) != -1:
                next_word = strng[index : strng.find(' ', index)]
                index = strng.find(' ', index)+1
            else:
                next_word = strng[index : ]
                index = len(strng)
                
            words.append(next_word)
        else:
            index+=1
  
    return words
    
print(mysplit("To be or not to be, that is the question"))
print(mysplit("To be or not to be,that is the question"))
print(mysplit("   "))
print(mysplit(" abc "))
print(mysplit(""))
