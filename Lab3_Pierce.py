'''
Date: Sep 5, 2023
@author: Benjamin Pierce
This program calculates a person's body mass index (BMI).
'''
weight = int(input("Enter your weight in pounds:"))   #user enters weight in pounds
height = int(input("Enter your height in inches:"))   #user enters height in inches
BMI = weight * 703/height**2   #BMI formula
print(f"Your BMI is: {BMI:.2f}")   #print BMI

if 18.5 <= BMI <= 24.9:   #if and elif statements
        print("You are within normal range for your BMI.")
elif BMI < 18.5:
    print("You are underweight for your BMI.")
elif 25 <= BMI <= 29.9:
    print("You are overweight for your BMI.")
else:
    print("Your are medically obese.")