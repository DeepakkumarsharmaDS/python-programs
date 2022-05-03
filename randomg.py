import random
import math

#Taking input start range
start = int(input("Enter the start number:- "))

#Taking input of end range
end = int(input("Enter the end number:- "))

#generating random number
#between start and end
x = random.randint(start, end)
print("\n\tYou've only", 
       round(math.log(end - start + 1,2)),
       "chance to gusse the integer!\n")

#initializing the number of gusses
count = 0

#calculate minimum of range
#gusses depond on range
while count < math.log(end  - start + 1,2):
    count += 1

#take guss input from user
guess = int(input("guess a number:- "))

if x == guess:
    print("!congratulation you did it", count, "try")

elif x > guess:
    print("your guess is too small!")

elif x < guess:
    print("your guess is so high!")

if count >= math.log(end - start + 1, 2):
    print("\nThe number is %d" % x)
    print("\tBetter Luck Next time!")