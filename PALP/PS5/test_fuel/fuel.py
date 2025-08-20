def main():
    percent = convert(input("Fraction: "))
    print(gauge(percent))

def convert(fract):
    while True:
        try:
            n = fract.find("/")
            num = int(fract[0:n])
            den = int(fract[n+1:])

            if num/den <= 1:
                percent = round(num/den*100)
                return percent
            else:
                fract = input("Fraction: ")
                pass
        except(ZeroDivisionError, ValueError):
            raise

def gauge(percent):
    if percent >=99:
        return "F"
    elif percent <=1:
        return "E"
    else:
        return (str(percent) + "%")
if __name__=="__main__":
    main()
