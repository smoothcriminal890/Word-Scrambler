print("Welcome to the scrambled word game! A word will be scrambled and you have to guess it. If you get it right, you win a point!")
import random
chosen_words = [
    "apple", "banana", "cherry", "date", "elderberry", "firefly", "grape", 
    "honeydew", "igloo", "jackfruit", "kangaroo", "lemon", "mango", "nectarine", 
    "orange", "papaya", "quince", "raspberry", "strawberry", "tangerine", "ugli fruit", 
    "vanilla bean", "watermelon", "xigua", "yam", "zucchini"   ]
points = 0
for i in range(26):
    word = list(chosen_words[i])
    random.shuffle(word)
    scrambled_words = ''.join(word)
    print(scrambled_words)
    guess = input("What is the word? ")
    if guess == chosen_words[i]:
        print("Correct! You win a point!")
        points += 1
    else:
        print(f"Incorrect. The word was {chosen_words[i]}.")
print(f"You have {points} points out of 26.")