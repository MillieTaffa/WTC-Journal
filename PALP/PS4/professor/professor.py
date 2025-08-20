import random

def main():
    score = 0
    i = 0
    level = get_level()

    while i < 10:
        x = generate_integer(level)
        y = generate_integer(level)
        tries = 0
        while tries < 3:
            try:
                ans = int(input(f"{x} + {y} = "))
            except ValueError:
                print("EEE")
                tries += 1
                continue

            if ans == x + y:
                score += 1
                break
            else:
                print("EEE")
                tries += 1

        if tries == 3:
            print(f"{x} + {y} = {x + y}")
        i += 1

    print("Score:", score)


def get_level():
    while True:
        try:
            level = int(input("Level (1, 2, or 3): "))
            if level in [1, 2, 3]:
                return level
        except ValueError:
            pass


def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    else:
        return random.randint(100, 999)
if __name__ == "__main__":
    main()
