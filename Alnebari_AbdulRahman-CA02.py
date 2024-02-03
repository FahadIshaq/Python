'''
Family Name:  Alnebari

Given Name:  Abdulrahman

University ID:  201691028

Month of Coding:  10th 

Year of Coding: 2023 

Problem Description:  
In this problem we have to actually take 2 user inputs one is the angle and the other is the travel time. We have to calculate the distance, 
the horizontal distance travelled by the Robor, the vertical distance travelled by the robot. We have to check for the usage of the battery. 
Based on the condition of the battery usage we have to make decision. The complete flow of the program is given below.
'''
import math #importing math to use the built in functions of mathematics
# taking user inputs

angle_in_degrees = float(input("Enter angle in degrees (0 to 90 inclusive): "))
time_in_seconds = float(input("Enter time of travel in seconds: "))

# constants used in the program 
speed = 1.5  # speed is initialized to 1.5s 
usage_of_battery_ps = 2.7 / 100  # to have 2.7%    


total_distance = speed * time_in_seconds#total_distance travelled by the robot 

horizontal_total_distance = total_distance * math.sin(math.radians(angle_in_degrees))  #horizontal total_distance covered by the robot


vertical_total_distance = total_distance * math.cos(math.radians(angle_in_degrees)) #vertical total_distance travelled by the robot.

battery_used = time_in_seconds * usage_of_battery_ps  ##battery estimate calculation

remaining_battery = 100 - battery_used #checking the achievement of the robot 

if remaining_battery < 0:#calculation on the remaining battery 



    
    print("The robot cannot reach its destination with the remaining battery.") #cannot reach the destination
    print(f"Distance traveled: {total_distance} meters") #total_distance travelled
    print(f"Horizontal movement: {horizontal_total_distance} meters")#horizontal movement
    print(f"Vertical movement: {vertical_total_distance} meters")#vertical movement
    print(f"Battery used: {battery_used:.2f}%")#battery usage
    print(f"Battery remaining: {remaining_battery:.2f}%")#battery remaining 
    print("The robot cannot return along the same path.") #can robot return to the same path 
    
else: #else condition
    print("The robot can reach its destination with the remaining battery.")
    print(f"Distance traveled: {total_distance} meters")#total_distance travelled
    print(f"Horizontal movement: {horizontal_total_distance} meters")#horizontal movement
    print(f"Vertical movement: {vertical_total_distance} meters")#vertical movement
    print(f"Battery used: {battery_used:.2f}%")#battery usage
    print(f"Battery remaining: {remaining_battery:.2f}%")#battery remaining 
    print("The robot can return along the same path if needed.")#can robot return to the same path 
