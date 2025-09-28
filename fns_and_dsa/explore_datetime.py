from datetime import datetime, timedelta

def display_current_datetime():
    """
    Get and print current date and time in format YYYY-MM-DD HH:MM:SS.
    Saves the current date/time in a variable named `current_date` and returns it.
    """
    current_date = datetime.now()
    print("Current date and time:", current_date.strftime("%Y-%m-%d %H:%M:%S"))
    return current_date

def calculate_future_date(current_date, days_to_add):
    """
    Calculate and print the future date after adding days_to_add to current_date.
    Saves the result in a variable named `future_date` and returns it.
    """
    future_date = current_date + timedelta(days=days_to_add)
    print("Future date:", future_date.strftime("%Y-%m-%d"))
    return future_date

def main():
    # Part 1: display current date/time and keep the date in current_date
    current_date = display_current_datetime()

    # Part 2: prompt user for days (exact prompt string)
    try:
        days = int(input("Enter the number of days to add to the current date: "))
    except ValueError:
        print("Invalid input. Please enter an integer number of days.")
        return

    # calculate and display future date (saves in future_date)
    calculate_future_date(current_date, days)

if __name__ == "__main__":
    main()
