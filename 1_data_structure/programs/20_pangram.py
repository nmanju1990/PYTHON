sentence = input("Enter a sentence: ").lower()
alphabet = "abcdefghijklmnopqrstuvwxyz"

for letter in alphabet:
    if letter not in sentence:
        print("It is not a pangram")
        break   
else:
    
    print("It is a pangram")
