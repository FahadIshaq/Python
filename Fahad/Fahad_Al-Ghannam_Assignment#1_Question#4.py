hours = int(input("Enter the hours of cardio exercise: "))
minutes = int(input("Enter the additional minutes of cardio exercise: "))
seconds = int(input("Enter the seconds of cardio exercise: "))

total_minutes = (hours * 60) + minutes + (seconds / 60)

print(f"Total time in minutes: {total_minutes}")
