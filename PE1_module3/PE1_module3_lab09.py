word_without_vowels = ""

# Prompt the user to enter a word
# and assign it to the user_word variable.

user_word = input("Enter a word: ").upper()

for letter in user_word:
    # Complete the body of the for loop.
    
    if letter in ['A','E','I','O','U']:
        continue
    else:
        word_without_vowels += letter

print(word_without_vowels)
