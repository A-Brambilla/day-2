"""
#Data Types
#String
print("Hello"[4])
print("123" + "345")
#Interger
print(123 + 345)
123_456_789
#Float  
3141.59
#Boolean
True
False
"""

#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

print("Welcome to the tip calculator")
total = float(input("What was the total bill? "))
split = int(input("How many people will split the bill? "))
ptip = int(input("I know tipping is stupid, but what percentage? "))

eachpersonpays = (total / split) * (1 + ptip/100)
result = round(eachpersonpays, 2)
result = "{:.2f}".format(eachpersonpays)
print(f"Each person should pay: {result}")