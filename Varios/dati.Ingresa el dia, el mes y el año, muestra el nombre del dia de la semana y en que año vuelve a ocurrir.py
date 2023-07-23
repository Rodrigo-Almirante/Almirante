import calendar

# Clear screen using ANSI VT100 codes
print("\033[H\033[J") 

# Ask for day, month and year
day = int(input("Enter the day (1-31): "))
month = int(input("Enter the month (1-12): "))
yeari = int(input("Enter the year (1900-2100): "))

# Determine the day name
day_name = calendar.day_name[calendar.weekday(yeari, month, day)]
month_name = calendar.month_name[month]

# Print the day name
print(f"\nThe day is {day_name} {day} of {month_name}\n")

# Print the years that the day of the week occurs
for year in range(1900, 2101):
    if calendar.weekday(year, month, day) == calendar.weekday(yeari, month, day):
        print(year, end=", ")

print("\n")