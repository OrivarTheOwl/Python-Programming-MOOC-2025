from datetime import datetime, timedelta

date_data = {}

if True:

    filename = input("Filename: ")
    start_date = input("Starting date: ")
    start_date = datetime.strptime(start_date, "%d.%m.%Y")
    og_start_date = datetime.strftime(start_date, "%d.%m.%Y")
    day_count = int(input("How many days: "))

    print("Please type in screen time in minutes one ach day (TV computer mobile): ")

    for day in range(day_count):
        new_date = start_date + timedelta(days=day)
        new_date = datetime.strftime(new_date, "%d.%m.%Y")
        date_data[new_date] = input(f"Screen time {new_date}: ")

else:
    test_inputs = {
        "filename": "late_june.txt",
        "start_date": "24.6.2020",
        "day_count": 5,
        "screen_times": [
            "60 120 0",
            "0 0 0",
            "180 0 0",
            "25 240 15",
            "45 90 5"
        ]
    }

    filename = test_inputs["filename"]
    start_date = datetime.strptime(test_inputs["start_date"], "%d.%m.%Y")
    og_start_date = datetime.strftime(start_date, "%d.%m.%Y")
    day_count = test_inputs["day_count"]

    print("Please type in screen time in minutes on each day (TV computer mobile):")

    for day in range(day_count):
        new_date = start_date + timedelta(days=day)
        new_date = new_date.strftime("%d.%m.%Y")
        date_data[new_date] = test_inputs["screen_times"][day]


total_mins = 0

for date, minutes in date_data.items():
    min_list = minutes.split(" ")
    for time in min_list:
        total_mins += int(time)

avg_mins = total_mins / day_count

open(filename, "w").close()
with open(filename, "a") as new_file:
    new_file.write(f"Time period: {og_start_date}-{new_date}\n")
    new_file.write(f"Total minutes: {total_mins}\n")
    new_file.write(f"Average minutes: {avg_mins}\n")
    for date in date_data:
        slash_mins = date_data[date].replace(" ", "/")
        new_file.write(f"{date}: {slash_mins}\n")

print(f"Data stored in file {filename}")