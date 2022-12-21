#Write your code below this line 👇
#Hint: Remember to import the random module first. 🎲
import random

test_seed = input("Create a Seed number: ")
random.seed(test_seed)

random_number = random.randint(0, 1)
# random_number2 = random.random()

# rnd_no = random_number * random_number2

if random_number == 1:
    print("Heads")
else:
    print("Tails")