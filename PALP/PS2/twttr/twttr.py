def main():
    userInput = shorten(input("Input: "))
    print(userInput)

def shorten(word):
    newWord = ''
    for letter in word:
        if letter.lower() not in ['a', 'e', 'i', 'o', 'u']:
            newWord += letter
    return newWord

if __name__=='__main__':
    main()