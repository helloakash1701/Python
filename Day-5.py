# Day-5

# 5.1
# You are going to write a program that calculates the average score from a List of scores.
                # heights = []
                # j = int(input("How many heights are there? "))
                # i = 0
                # while i <  j:
                #     height = float(input("Enter your height "))
                #     heights.append(height)
                #     i = i + 1
                # print(heights)
                # avg = 0
                # for h in heights :
                #     avg = h + avg
                # score = avg/j
                # print(f"student_scores {score.__round__()}")

# 5.2
# You are going to write a program that calculates the highest score from a List of scores.

                # nums = []
                # i = 0
                # j = int(input("How many numbers do you want in a list? "))

                # while i < j :
                #     num = int(input("Enter numbers "))
                #     nums.append(num)
                #     i = i+1
                # print(nums)
                # ln = 0
                # for n in nums :
                #     if i > ln :
                #         ln = n
                #         print(f"Highest score {ln}")

# 5.3
# You are going to write a program that calculates the sum of all the even numbers from 1 to 100. Thus, the first even number would be 2 and the last one is 100: i.e. 2 + 4 + 6 + 8 +10 ... + 98 + 100

                # total = 0
                # for num in range(1,101):
                #     # print(i)
                #     if num % 2 == 0:
                #         total = total + num
                # print(total)    

# 5.4
# You are going to write a program that automatically prints the solution to the FizzBuzz game.

                # for i in range(1,100):
                #     if i % 3 == 0 :
                #         print("FIZZ")
                #     elif i % 5 == 0 :
                #         print("BUZZ")
                #     elif i % 3 == 0 and i % 5 == 0:
                #         print("FIZZ BUZZ")
                #     else :
                #         print(i)

# Password Generator

#Password Generator Project
                # import random
                # letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
                # numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
                # symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
                # password = []
                # print("Welcome to the PyPassword Generator!")
                # nw= int(input("How many letters would you like in your password?\n")) 
                # ns = int(input(f"How many symbols would you like?\n"))

                # while ns > nw :
                #     ns = int(input(f"How many symbols would you like?\n"))
                # nn = int(input(f"How many numbers would you like?\n"))
                # while nn > nw :
                #     nn = int(input(f"How many numbers would you like?\n"))



                # nw = nw - ( nn + ns)
                # print(f"nw is {nw}")
                # i = 0 
                # while i < nw :
                #     l = random.choice(letters)
                #     i = i +1
                #     password.append(l)

                # for i in range(ns):
                #     i = random.choice(symbols)
                #     password.append(i)

                # for j in range(nn):
                #     j = random.choice(numbers)
                #     password.append(j)

                # print(''.join(password))





