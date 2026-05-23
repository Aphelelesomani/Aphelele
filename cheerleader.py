word = input("Enter your favourite word: ")
vowels = [ "a", "e", "i", "o", "u"]
for letters in word:    
    if letters.lower()in vowels:
        print(f" Give me an {letters.upper()}")
    else:
        print(f"What does it say?????? {word.upper()}!!!!!!")
