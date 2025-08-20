def main():
    userInput=input("Input: ")
    print(shorten(userInput))


def shorten(word):
    vowels = ["a", "e", "i", "o", "u"]

    for vowel in word:
        if vowel.lower() in vowels:
            word = word.replace(vowel, "")
    return word


if __name__ == "__main__":
    main()

