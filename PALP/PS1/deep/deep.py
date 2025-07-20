def deep():
    userInput = input("What is the Answer to Great Question of Life, the Universe and Everything: ").strip(" ").lower()
    if userInput == "42" or userInput== "forty two" or userInput=="forty-two":
        print("Yes")
    else:
        print('No')

deep()