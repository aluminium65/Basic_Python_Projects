import random

score = 0
questions = 0

operators = ['+', '-', '*', '/']

print ('''

#######  ###  ##### #   #     ####  #   # ##### ##### 
#  #  # #   #   #   #   #    #    # #   #   #      #
#  #  # #####   #   #####    #   &# #   #   #     #
#     # #   #   #   #   #     ####&  ###  #####  ##### 
                                   &

------------------------------By aluminium----------------------------------     
''')
print("[GITHUB] https://github.com/aluminium65/")
print (" \n \n Welcome to the Math Quiz!")
print ("You will be asked 10 simple arithematic questions.")

p = input("Press Enter to begin")








while questions < 10:
  x = random.randint(1,12)
  y = random.randint(1,12)
  z = random.choice(operators)

  x = int(x)
  y = int(y)
  questions += 1
  print (f"----- --Question '{questions}' of '10'-- -----")
  if z == '/':
    y = random.randint(1,12)
    M = random.randint(1,12)
    x = y * M
    x = int(x)
    y = int(y)
  question = f"What is {int(x)}{z}{int(y)}"
  print (question)
  answer = 0
  if z == '+':
    answer = x + y
  elif z == '-':
    answer = x - y
  elif z == '*':
    answer = x * y
  elif z == '/':
    answer = x / y
  try:
    user_input = input("Enter your Answer: ")
    user_input = int(user_input)
  except ValueError:
    print ("Invalid Input. Please Enter a Whole Number.")
    questions -= 1
    continue
  if user_input == answer:
    print ("Correct\n")
    score += 1
  else:
    print (f"Wrong Answer. The Right one is {int(answer)}")

print ("Game Over!")
print (f"You Scored {score} out of 10")
