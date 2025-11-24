# explore_datetime.py
from datetime import datetime, timedelta

# Part 1: Display current date and time
def display_current_datetime():
    current_date = datetime.now()  # store current date/time
    print("Current date and time:", current_date.strftime("%Y-%m-%d %H:%M:%S"))
    return current_date

# Part 2: Calculate future date
def calculate_future_date(current_date):
    days = int(input("Enter the number of days to add to the current date: "))
    future_date = current_date + timedelta(days=days)  # calculate future date
    print("Future date:", future_date.strftime("%Y-%m-%d"))
    return future_date

# Run the functions in sequence
current_date = display_current_datetime()
calculate_future_date(current_date)

