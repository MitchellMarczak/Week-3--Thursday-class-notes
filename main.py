x = 5
x += 3
print(x)
x = 5
x -= 4
print(x)
x = 5
x /= 5
print(x)

x = "john"
x += "smith"
print(x)
question_1_users_answer = input("What keys do you typically use to moves your character forward in videogames?(use lowercase letters)\n")
question_1_answer = "wasd"
final_answer = question_1_answer == question_1_users_answer
if(final_answer == True):
  print("You answered with the correct answer of '" + question_1_users_answer + "'!")
if(final_answer == False):
  print("Your answer of '" + question_1_users_answer + "' was incorrect! The correct answer was '" + question_1_answer + "'!") 

