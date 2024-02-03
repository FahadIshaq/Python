def calculate_total_time_in_minutes(hours, minutes, seconds): 
    totalTimeInMinutes = hours * 60 + minutes + seconds / 60 
    return totalTimeInMinutes
hours = float(input("Enter the hours spent on Cardio exercise: "))
minutes = float(input("Enter the minutes spent on Cardio exercise: "))
seconds = float(input("Enter the seconds spent on Cardio exercise: "))
totalTimeInMinutes = calculate_total_time_in_minutes(hours, minutes, seconds)
print(f"The total time in minutes is: {totalTimeInMinutes:.2f}")

