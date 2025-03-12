print("Hello ! Welcome to the geography quiz !!")

q1 = input("Do you want to play? :) ")

if q1.lower().strip() != "yes":
    quit()
print("...")
score = 0     
    
q2 = input("Which is the largest continent by land area? ")  

if q2.lower().strip() != "asia":
    print("Incorrect !")     
else:
    print("Correct !") 
    score += 1   

print("...")

q3 = input("What is the capital of France? ")  

if q3.lower().strip() != "paris":
    print("Incorrect !")     
else:
    print("Correct !")  
    score += 1  

print("...")

q4 = input("Which ocean is the largest? ")  

if q4.lower().strip() != "pacific" and q4.lower().strip() != "pacific ocean":
    print("Incorrect !")     
else:
    print("Correct !")  
    score += 1  

print("...")

q5 = input("Which country is famous for its pyramids? ")  

if q5.lower().strip() != "egypt":
    print("Incorrect !")     
else:
    print("Correct !")   
    score += 1 

print("...")

q6 = input("What is the longest river in the world? ")  

if q6.lower().strip() != "amazon" and q6.lower().strip() !="amazon river":
    print("Incorrect !")     
else:
    print("Correct !")  
    score += 1  

print("...")

q7 = input("Which country is famous for the Great Wall? ")  

if q7.lower().strip() != "china":
    print("Incorrect !")     
else:
    print("Correct !")
    score += 1       
    
print("Quiz ends !")
print(f"You got {score} out of 6 correct !")
percentage = round((score/6)*100,2)
print(f"Correct percentage = {percentage}%")

if percentage > 35:
    print("You passed ;)")
else:
    print("You failed :(")  
