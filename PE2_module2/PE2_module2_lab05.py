def are_anagrams(text1, text2):
    text_1 = text1.lower()
    text_2 = text2.lower()
    
    if text1 == text2:
        return 'Anagrams' if (text1 != '') else 'Not anagrams'
        
    for t1 in text_1:
        if text_1.count(t1) != text_2.count(t1):
            return "Not anagrams"
    return "Anagrams"
    
s1 = input("Enter text 1: ")
s2 = input("Enter text 2: ")
print(are_anagrams(s1,s2))
