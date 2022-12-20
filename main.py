# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
Lower1 = name1.lower()
Lower2 = name2.lower()
Two_name = Lower1 + " " + Lower2

Love1 = Two_name.count('t')
Love1 += Two_name.count('r')
Love1 += Two_name.count('u')
Love1 += Two_name.count('e')

Love2 = Two_name.count('l')
Love2 += Two_name.count('o')
Love2 += Two_name.count('v')
Love2 += Two_name.count('e')
Love_Score = Love1 * 10 + Love2

if (Love_Score < 10 or Love_Score > 90):
  print(f"Your score is {Love_Score}, you go together like coke and mentos.")
elif (Love_Score > 40 or Love_Score < 50):
  print(f"Your score is {Love_Score}, you are alright together.")
else :
  print(f"Your score is {Love_Score}.")