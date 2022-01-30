# Day 2 of 100 days challenge

# 2.1
# Write a program that adds the digits in a 2 digit number. e.g. if the input was 35, then the output should be 3 + 5 = 8


                # two_digit_number = int(input("Type a two digit number: "))
                # two_digit_number = str(two_digit_number)
                # two_digit_number_1 = int(two_digit_number[0])
                # two_digit_number_2 = int(two_digit_number[1])
                # sum = two_digit_number_1 +two_digit_number_2
                # print("The output is",sum)
        
# 2.2 
# Write a program that calculates the Body Mass Index (BMI) from a user's weight and height.

                # height = float(input("enter your height in m: "))
                # weight = float(input("enter your weight in kg: "))
                # bmi = weight/((height)**2)
                # print(bmi.__round__())

# 2.3
# Create a program using maths and f-Strings that tells us how many days, weeks, months we have left if we live until 90 years old.

                # age = int(input("What is your current age? "))
                # years_left = 90 - age
                # print(f"Total years left: {years_left}")
                # total_days_left = years_left * 365 
                # print(f"Total days left: {total_days_left}")
                # total_months_left = years_left*12
                # print(f"Total months left: {total_months_left}")
                # total_weeks_left = 52 * years_left
                # print(f"Total weeks left: {total_weeks_left}")


# Tip calculator

                # print("Welcome to the tip calculator!")
                # total_bill = float(input("What was the total bill? "))
                # total_tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
                # split_mem = int(input("How many people to split the bill? "))
                # total_bill_with_tip = ((total_bill * total_tip)/100)+total_bill
                # print(total_bill_with_tip)
                # total_money_after_splitting = total_bill_with_tip/split_mem
                # print(f"Each person should pay: ${round(total_money_after_splitting,2)}")
