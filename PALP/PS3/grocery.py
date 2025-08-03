def main():
    groceryList = {}
    while True:
        try:
            item = input().strip().lower()
            if item:
                groceryList[item] = groceryList.get(item,0)+1
        except EOFError:
            break
    for item in sorted(groceryList):
        count = groceryList[item]
        print(f"{count} {item.upper()}")
if __name__ == "__main__":
    main()
