import datetime
def calculate_countdown(target_date):
 current_date = datetime.datetime.now()
 time_left = target_date - current_date
 return time_left

# Get the target date from the user
target_date_str = input("Enter the target date (DD-MM-YYYY): ")
target_date = datetime.datetime.strptime(target_date_str, "%d-%m-%Y")

# Calculate the countdown
countdown = calculate_countdown(target_date)

# Display the countdown
days = countdown.days
hours, remainder = divmod(countdown.seconds, 3600)
minutes, seconds = divmod(remainder, 60)
print("Countdown:")
print("Days:", days)
print("Hours:", hours)
print("Minutes:", minutes)
print("Seconds:", seconds)