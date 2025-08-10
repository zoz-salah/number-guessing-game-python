import random

print("--------------------------")
print("🎲𝓷𝓾𝓶𝓫𝓮𝓻 𝓰𝓾𝓮𝓼𝓼𝓲𝓷𝓰 𝓰𝓪𝓶𝓮🎲")
print("--------------------------")

number = random.randint(1, 10)

def game(number):
    guess = int(input("🔢 Guess a number from 1 ➡️ 10 : "))
    if guess == number and 1 <= guess <= 10:
        print(f"🤜 OOOHHH your guess is right! The number was {number}")
    elif guess > number and 1 <= guess <= 10:
        print("🙅‍♂️ NOOP your guess is higher")
        print("🔄️ Try again now broo 🔄️")
        game(number)
    elif guess < number and 1 <= guess <= 10:
        print("🙅‍♂️ NOOP your guess is lower")
        print("🔄️ Try again now broo 🔄️")
        game(number)
    else:
        print("🤢 WRONG INPUT")

game(number)
