#exersie 1
# 🚨 Don't change the code below 👇
#number = int(input("Which number do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
#if number%2 == 0:
 #   print(str(number)+ " is even")
#else:
 #   print(str(number)+ " is odd")


#ex 2

# 🚨 Don't change the code below 👇

import math


#height = float(input("enter your height in m: "))
#weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#It should tell them the interpretation of their BMI based on the BMI value.
#Under 18.5 they are underweight
#Over 18.5 but below 25 they have a normal weight
#Over 25 but below 30 they are slightly overweight
#Over 30 but below 35 they are obese
#Above 35 they are clinically obese.

#Write your code below this line 👇
#bmi = math.ceil(weight/(height*height))

#if bmi < 18.5:
#    print("Your BMI is " + str(bmi) + ", you are underweight.")
#elif bmi > 18.5 and bmi < 25.0:
#   print("Your BMI is " + str(bmi) + ", you have a normal weight.")
#elif bmi > 25 and bmi < 30:
#   print("Your BMI is " + str(bmi) + ", you are slightly overweight.")
#elif bmi > 30 and bmi < 35.0:
#   print("Your BMI is " + str(bmi) + ", you are obese.")
#elif bmi > 35:
#   print("Your BMI is " + str(bmi) + " you are clinically obese.")

# ex 3
#This is how you work out whether if a particular year is a leap year.
#on every year that is evenly divisible by 4 
#**except** every year that is evenly divisible by 100 
#**unless** the year is also evenly divisible by 400

# 🚨 Don't change the code below 👇
#year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

#if year%4 == 0 and (not(year%100 == 0) or year%400 ==0):
#    print("Leap year")
#else:
#    print("Not Leap year")


#ex 4
#Based on a user's order, work out their final bill.
#Small Pizza: $15
#Medium Pizza: $20
#Large Pizza: $25
#Pepperoni for Small Pizza: +$2
#Pepperoni for Medium or Large Pizza: +$3
#Extra cheese for any size pizza: + $1

# 🚨 Don't change the code below 👇
#print("Welcome to Python Pizza Deliveries!")
#size = input("What size pizza do you want? S, M, or L ")
#add_pepperoni = input("Do you want pepperoni? Y or N ")
#extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

#if size == "S":
 #   bill = 15
#elif size == "M":
 #   bill = 20
#elif size == "L":
#    bill = 25

#if add_pepperoni == "Y":
   #3 if size == "S":
  #     bill = bill + 2
 #   else:
#        bill = bill + 3

#if extra_cheese == "Y":
 #   bill = bill + 1

#print("Your final bill is: $" + str(bill) + ".")

# 🚨 Don't change the code below 👇
#print("Welcome to the Love Calculator!")
#name1 = input("What is your name? \n")
#name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

#full_name = (name1 + name2).lower()
#true_score = 0
#love_score = 0
#3love = "love"
#3true = "true"

#for x in true:
#    true_score = true_score + full_name.count(x)
    
#for x in love:
#    love_score = love_score + full_name.count(x)

#love_count = str(true_score)+ str(love_score)

#if int(love_count) <10 or int(love_count)> 90:
#    print("Your score is " + love_count + ", you go together like coke and mentos.")
#elif 40 < int(love_count) < 50:
#    print("Your score is " + love_count + ", you alright together.")
#else:
#   print("Your score is " + love_count + ".")

#Project Day 3

print("Welcome to Treasure Island, your mission is to find the treasure")
response = input("You are at crossroad, which way are you gonna get, left or right?")
if response == "left":
    print("GAME OVER")
else:
    response = input("You came accros a lake. You see a ferry on the distance. Will you wait for the ferry or \"swim\" through the lake?")
    if response == "swim":
        print("GAME OVER")
    else:
        response = input("Once you crossed the lake You arrived to a castle with three doors, a yellow to the left, blue on the center and red on the right. One of those doors will lead you to the final treasure. Which one would you choose")
        if response == "red":
            print("You win")
        else:
            print("GAME OVER")
           


