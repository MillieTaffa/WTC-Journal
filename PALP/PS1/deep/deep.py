def main():
    userInput = input("What is the answer to the Great Question Of Life, the Universe, and Everything? ")

    if userInput == "42" or userInput.lower() == 'forty-two' or userInput.lower() == 'forty two':
        print('Yes')
    else:
        print('No')

main()