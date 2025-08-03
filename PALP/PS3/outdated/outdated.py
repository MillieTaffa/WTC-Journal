def main():
    months = {
        "January": "01", "February": "02", "March": "03", "April": "04",
        "May": "05", "June": "06", "July": "07", "August": "08",
        "September": "09", "October": "10", "November": "11", "December": "12"
    }

    while True:
        try:
            dateInput = input("Date: ").strip()

            if "/" in dateInput:
                parts = dateInput.split("/")
                if len(parts) != 3:
                    raise ValueError
                month, day, year = map(int, parts)
                if not (1 <= month <= 12 and 1 <= day <= 31):
                    raise ValueError
                print(f"{year:04}-{month:02}-{day:02}")
                break

            elif "," in dateInput:
                month_str, rest = dateInput.split(" ", 1)
                if month_str not in months:
                    raise ValueError
                day_str, year = rest.split(",")
                day = int(day_str.strip())
                year = int(year.strip())
                if not (1 <= day <= 31):
                    raise ValueError
                print(f"{year:04}-{months[month_str]}-{day:02}")
                break
            else:
                raise ValueError
        except (ValueError, KeyError):
            pass
if __name__ == "__main__":
    main()
