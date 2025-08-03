def getFrac():
    while True:
        try:
            frac = input("Fraction (X/Y): ").strip()
            x_str, y_str = frac.split('/')
            x,y = int (x_str), int(y_str)

            if y==0:
                raise ZeroDivisionError("Denominator can't be zero")
            if x>y:
                raise ValueError("Numerator can't be bigger than denominator")
            if x<0 or y<0:
                raise ValueError("Positive intergers only")
            return x,y

        except(ValueError, ZeroDivisionError):
            print("Invalid input")

def main():
    x,y = getFrac()
    perc = round((x/y)*100)
    if perc <= 1:
        print("E")
    elif perc >=99:
        print("F")
    else:
        print(f"{perc}%")
if __name__ == "__main__":
    main()
