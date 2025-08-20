import random

def main():
    level = get_level()
    random_num = random.randint(1,level)
    get_guess(random_num)

def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level <= 0:
                continue
            return level
        except ValueError:
            continue

def get_guess(random_num):
    while True:
        try:
            guess = int(input("Guess: "))
            if guess <= 0:
                continue
            elif guess < random_num:
                print("Too small!")
                continue
            elif guess > random_num:
                print("Too large!")
                continue
            elif guess == random_num:
                print("Just right!")
        except ValueError:
            continue
        return guess
    print(guess)
if __name__ == "__main__":
    main()
