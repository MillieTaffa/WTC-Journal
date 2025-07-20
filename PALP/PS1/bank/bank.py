def bank():
    userInput = input("Greeting: ").lower().strip()

    if userInput.startswith("hello"):
        print("You get $0")
    elif userInput.startswith("h"):
        print("You get $20")
    else:
        print("You get $100")
bank()
