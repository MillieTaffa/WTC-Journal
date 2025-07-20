def main():
    time = input("time: ")
    cTime = convert(time)
    if cTime >= 7 and cTime <= 8:
        print("breakfast time")
    elif cTime >= 12 and cTime <= 13:
       print("lunch time")
    elif cTime >= 18 and cTime <= 19:
       print("dinner time")

def convert(time):
    hours, minutes = time.split(":")
    hours = float(hours)+ (float(minutes)/60)
    return hours


if __name__ == "__main__":
    main()
