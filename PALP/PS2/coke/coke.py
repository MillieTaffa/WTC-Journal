def coke():
    amount_due = 50
    coins = [5, 10, 25]
    while amount_due > 0:
        print(f"Amount Due: {amount_due}")
        try:
            coin = int(input("Insert Coin: "))
            if coin in coins:
                amount_due -= coin
            else:
                pass
        except ValueError:
            continue

    print(f"Change Owed: {abs(amount_due)}")

coke()