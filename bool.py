"""
practicing boolean
"""
import random

truethy = True
falsy = False

age = 20
is_over_age = age >= 18

#print (is_over_age)

rand_num = random.randint(1,100)

user_num = int(input("Please enter a number: "))

print (rand_num == user_num)