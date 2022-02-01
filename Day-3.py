# Day-3

# # 3.1
# Write a program that works out whether if a given number is an odd or even number.

                # number = int(input("Which number do you want to check? "))
                # if number % 2 ==0 :
                #     print("This is an even number.")
                # else :
                #     print("This is an odd number.")

# 3.2
# Write a program that interprets the Body Mass Index (BMI) based on a user's weight and height.
# It should tell them the interpretation of their BMI based on the BMI value.
# Under 18.5 they are underweight
# Over 18.5 but below 25 they have a normal weight
# Over 25 but below 30 they are slightly overweight
# Over 30 but below 35 they are obese
# Above 35 they are clinically obese


                # height = float(input("enter your height in m: "))
                # weight = float(input("enter your weight in kg: "))
                # bmi = weight/((height)**2)
                # if bmi < 18.5 :
                #     print(f"Your BMI is {bmi.__round__()}, you are underweight.")
                # elif bmi >= 18.5 and bmi < 25:
                #     print(f"Your BMI is {bmi.__round__()}, you have a normal weight.")
                # elif bmi >= 25 and bmi < 30:
                #     print(f"Your BMI is {bmi.__round__()}, you are slightly overweight.")
                # elif bmi >= 30 and bmi < 35:
                #     print(f"Your BMI is {bmi.__round__()}, you are obese.")
                # elif bmi >35:
                #     print(f"Your BMI is {bmi.__round__()}, you are clinically obese.")

# 3.3
# Write a program that works out whether if a given year is a leap year. A normal year has 365 days, leap years have 366, with an extra day in February. The reason why we have leap years is really fascinating, this video does it more justice:



                # year = int(input("Which year do you want to check? "))
                # if year % 4 == 0 and year % 100 != 0: 
                #    print("Its a leap year ")
                # elif year % 4 ==0 and year %100 ==0 and year %400 ==0 :
                #     print("Its a leap year ")
                # else :
                #     print("Its not a leap year ")


# 3.4
# Congratulations, you've got a job at Python Pizza. Your first job is to build an automatic pizza order program.

# Based on a user's order, work out their final bill.

# Small Pizza: $15
# Medium Pizza: $20
# Large Pizza: $25
# Pepperoni for Small Pizza: +$2
# Pepperoni for Medium or Large Pizza: +$3
# Extra cheese for any size pizza: + $1

                # S = 15
                # M = 20
                # L = 25
                # Ps = 2
                # Pm = 3
                # Ec = 1

                # print("Welcome to Python Pizza Deliveries!")
                # size = input("What size pizza do you want? S, M, or L: ")

                # if size == "S":
                #     bill = S
                #     add_pepperoni = input("Do you want pepperoni? Y or N: ")
                #     if add_pepperoni == "Y":
                #         bill = bill + Ps
                #         extra_cheese = input("Do you want extra cheese? Y or N: ") 
                #         if extra_cheese == "Y":
                #             bill = bill + Ec
                #         else :
                #             bill = bill
                #         print(f"Your final bill is: ${bill}")

                # if size == "M":
                #     bill = M
                #     add_pepperoni = input("Do you want pepperoni? Y or N: ")
                #     if add_pepperoni == "Y":
                #         bill = bill + Pm
                #         extra_cheese = input("Do you want extra cheese? Y or N: ") 
                #         if extra_cheese == "Y":
                #             bill = bill + Ec
                #         else :
                #             bill = bill
                #         print(f"Your final bill is: ${bill}")

                # if size == "L":
                #     bill = L
                #     add_pepperoni = input("Do you want pepperoni? Y or N: ")
                #     if add_pepperoni == "Y":
                #         bill = bill + Pm
                #         extra_cheese = input("Do you want extra cheese? Y or N: ") 
                #         if extra_cheese == "Y":
                #             bill = bill + Ec
                #         else :
                #             bill = bill
                #         print(f"Your final bill is: ${bill}")

# 3.5
# Love calculator




                # from re import S


                # print("Welcome to the Love Calculator!")
                # name1 = input("What is your name? \n")
                # name2 = input("What is their name? \n")
                # # Python3 program to Split string into characters
                # def split(word):
                # 	return [char for char in word]
                    
                # # Driver code
                # word = name1
                # def split(word2):
                # 	return [char for char in word2]
                # word2 = name2
                # spl_name1 = split(word)
                # spl_name2 = split(word2)
                # print(spl_name1,spl_name2)
                # t_count = 0
                # r_count = 0
                # u_count = 0
                # e_count = 0
                # l_count = 0
                # o_count = 0
                # v_count = 0
                # e2_count = 0
                # for i in spl_name1:
                #     if i =="T" :
                #         print("T occur")
                #         t_count = t_count+1
                #     else :
                #         print("T didnt occur")
                #     if i =="R" :
                #         print("R occur")
                #         r_count = r_count+1
                #     else :
                #         print("R didnt occur")
                #     if i =="U" :
                #         print("U occur")
                #         u_count = u_count+1
                #     else :
                #         print("U didnt occur")
                #     if i =="E" :
                #         print("E occur")
                #         e_count = e_count+1
                #     else :
                #         print("E didnt occur")
                # # print(f"T occur {t_count} R occur {r_count} U occur {u_count} E occur {e_count}")

                # for i in spl_name2:
                #     if i =="T" :
                #         print("T occur")
                #         t_count = t_count+1
                #     else :
                #         print("T didnt occur")
                #     if i =="R" :
                #         print("R occur")
                #         r_count = r_count+1
                #     else :
                #         print("R didnt occur")
                #     if i =="U" :
                #         print("U occur")
                #         u_count = u_count+1
                #     else :
                #         print("U didnt occur")
                #     if i =="E" :
                #         print("E occur")
                #         e_count = e_count+1
                #     else :
                #         print("E didnt occur")
                # print(f"T occur {t_count} R occur {r_count} U occur {u_count} E occur {e_count}")  
                # sum = t_count+r_count+u_count+e_count
                # sum = str(sum)
                # print(f"Total {sum}") 
                        
                # for i in spl_name1:
                #     if i =="L" :
                #         print("L occur")
                #         l_count = l_count+1
                #     else :
                #         print("L didnt occur")
                #     if i =="O" :
                #         print("O occur")
                #         o_count = o_count+1
                #     else :
                #         print("O didnt occur")
                #     if i =="V" :
                #         print("V occur")
                #         v_count = v_count+1
                #     else :
                #         print("V didnt occur")
                #     if i =="E" :
                #         print("E occur")
                #         e2_count = e2_count+1
                #     else :
                #         print("E didnt occur")
                # # print(f"L occur {l_count} O occur {o_count} V occur {v_count} E occur {e_count}")

                # for i in spl_name2:
                #     if i =="L" :
                #         print("L occur")
                #         l_count = l_count+1
                #     else :
                #         print("L didnt occur")
                #     if i =="O" :
                #         print("O occur")
                #         o_count = o_count+1
                #     else :
                #         print("O didnt occur")
                #     if i =="V" :
                #         print("V occur")
                #         v_count = v_count+1
                #     else :
                #         print("V didnt occur")
                #     if i =="E" :
                #         print("E occur")
                #         e2_count = e2_count+1
                #     else :
                #         print("E didnt occur")
                # print(f"L occur {l_count} O occur {o_count} V occur {v_count} E occur {e2_count}")  
                # sum2 = l_count+o_count+v_count+e2_count
                # sum2 = str(sum2)
                # print(f"Total {sum2}")         
                # love_score = int(sum + sum2)  
                # if  love_score > 90 :
                #     print(f"Your score is {love_score}, you go together like coke and mentos.")
                # elif love_score < 10 :
                #     print(f"Your score is {love_score}, you go together like coke and mentos.")
                # elif love_score <50 and love_score >40 :
                #     print(f"Your score is {love_score}, you are alright together.")
                # else :
                #     print(f"Your score is {love_score}")

# Day 3 final project 

# Treasure Island

                # from os import PRIO_PGRP


                # print('''
                # *******************************************************************************
                #           |                   |                  |                     |
                #  _________|________________.=""_;=.______________|_____________________|_______
                # |                   |  ,-"_,=""     `"=.|                  |
                # |___________________|__"=._o`"-._        `"=.______________|___________________
                #           |                `"=._o`"=._      _`"=._                     |
                #  _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
                # |                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
                # |___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
                #           |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
                #  _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
                # |                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
                # |___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
                # ____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
                # /______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
                # ____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
                # /______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
                # ____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
                # /______/______/______/______/______/______/______/______/______/______/_____ /
                # *******************************************************************************
                # ''')
                # print("Welcome to Treasure Island.")
                # print("Your mission is to find the treasure.") 
                # first_ques =  input("Would you like to go left or right? ")
                # first_ques = first_ques.isupper()
                # if first_ques ==  "RIGHT" :
                #     print("You've fallen into a hole")
                #     print("GAME OVER")
                # elif first_ques == "Left" or "LEFT" :
                #     second_ques = input("Swim or wait? ")
                #     second_ques = second_ques.isupper()
                #     if second_ques ==  "SWIM" :
                #         print("You've been attacked by a trout")
                #         print("GAME OVER")
                #     elif second_ques == "WAIT" :
                #         third_ques = input("Which door would you like to choose? Red or Blue ")
                #         third_ques = third_ques.isupper()
                #         if third_ques == "BLUE" :
                #             print("Eater by beast")
                #             print("GAME OVER")
                #         elif third_ques == "RED" :
                #             print("Burned by fire")
                #             print("GAME OVER")
                #         elif third_ques == "YELLOW" :
                #             print("YOU WON!")
                #         else :
                #             print("GAME OVER")
                        
                #     else:
                #         print("GAME OVER")
                # else :
                #     print("GAME OVER")
