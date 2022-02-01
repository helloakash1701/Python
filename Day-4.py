# Day-4

# 4.1
# You are going to write a virtual coin toss program. It will randomly tell the user "Heads" or "Tails".

                # import random as random
                # rand_int = random.randint(0,1)
                # if rand_int == 1 :
                #     print("Head")
                # else :
                #     print("Tail")

# 4.2
# You are going to write a program which will select a random name from a list of names. The person selected will have to pay for everybody's food bill.

                # from os import name

                # import random
                # names_string = input("Give me everybody's names, separated by a comma. ")
                # names = names_string.split(", ")
                # print(names)
                # print(len(names))
                # random_number = random.randint(0,len(names))
                # print(f"{names[random_number]} is going to buy the meal today!")

# 4.3
# You are going to write a program which will mark a spot with an X.


                # from numpy import piecewise


                # row1 = ["⬜️","⬜️","⬜️"]
                # row2 = ["⬜️","⬜️","⬜️"]
                # row3 = ["⬜️","⬜️","⬜️"]
                # map = [row1, row2, row3]
                # print(f"{row1}\n{row2}\n{row3}")
                # position = input("Where do you want to put the treasure? ")
                # column = int(position[0])
                # if column == 1 :
                #     column = column - 1
                # elif column == 2 :
                #     column = column - 1

                # elif column == 3 :
                #     column = column - 1

                # row = int(position[1])
                # if row == 1 :
                #     row1[column]= "⛳"
                # elif row == 2:
                #     row2[column] = "⛳"
                # elif row== 3:
                #     row3[column] = "⛳"
                # print(f"{row1}\n{row2}\n{row3}")

# PROJECT DAY 4 
# Make a rock, paper, scissors game.



                # import random

                # rock = '''
                #     _______
                # ---'   ____)
                #       (_____)
                #       (_____)
                #       (____)
                # ---.__(___)
                # '''

                # paper = '''
                #     _______
                # ---'   ____)____
                #           ______)
                #           _______)
                #          _______)
                # ---.__________)
                # '''

                # scissors = '''
                #     _______
                # ---'   ____)____
                #           ______)
                #        __________)
                #       (____)
                # ---.__(___)
                # '''
                # opt = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
                # comp_opt = random.randint(0,2)
                # print(f"Your input {opt}")
                # # User input
                # if opt == 0 :
                #     print(rock)
                # elif opt == 1:
                #     print(paper)
                # elif opt == 2:
                #     print(scissors)

                # # Computer input
                # print(f"Computer input is {comp_opt}")
                # if comp_opt == 0 :
                #     print(rock)
                # elif comp_opt == 1:
                #     print(paper)
                # elif comp_opt == 2:
                #     print(scissors)

                # if comp_opt == opt :
                #     print("No Damage ")
                # if opt == 0 and comp_opt <3 and comp_opt!= 1 :
                #     print(f"Winner rock {rock}")
                # elif opt == 1 and comp_opt == 0 or opt ==0 and comp_opt ==1:
                #     print(f"Winner Paper {paper}")
                # elif opt == 2 and comp_opt == 0 :
                #     print(f"Winner rock {rock}")
                # elif opt == 1 and comp_opt == 2 or opt == 2 and comp_opt == 1:
                #     print(f"Winner scissors {scissors}")





