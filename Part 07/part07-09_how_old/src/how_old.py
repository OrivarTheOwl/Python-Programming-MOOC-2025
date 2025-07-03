from datetime import datetime, timedelta

day = int(input("Day: "))
month = int(input("Month: "))
year = int(input("Year: "))

dob = datetime(year, month, day)
millennium = datetime(1999, 12, 31)

if dob < millennium:
    difference = millennium - dob
    print(f"You were {difference.days} days old on the eve of the new millennium.")
else:
    print("You weren't born yet on the eve of the new millennium.")