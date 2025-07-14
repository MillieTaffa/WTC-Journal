dollars = input("How much was the meal?: ")
percent = input("How much will you tip?: ")

tip = float(dollars)*float(percent)/100

print(f"Leave ${tip:.2}")