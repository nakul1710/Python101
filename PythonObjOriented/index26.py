import datetime

# Create a date object for a specific date
date = datetime.date(2025, 1, 2)
today = datetime.date.today()
print("Specific date:", date)
print("Today's date:", today)

# Create a time object for a specific time
time_obj = datetime.time(12, 30, 0)
print("Specific time:", time_obj)

# Get current date and time
now = datetime.datetime.now()
print("Current datetime:", now)

# Format current time and date
formatted_now = now.strftime("%H:%M:%S %d-%m-%y")
print("Formatted current datetime:", formatted_now)

# Correct usage to create a datetime object
target_datetime = datetime.datetime(2023, 1, 2, 12, 30, 1)
current_datetime = datetime.datetime.now()

if target_datetime < current_datetime:
    print("Target date has passed")
else:
    print("Target has not passed")