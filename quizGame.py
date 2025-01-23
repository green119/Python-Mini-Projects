print("Welcome to my Computer Quiz!!!")

playing = input("Do you want to play? ")

if playing.lower() != "yes": # also available upper()
    quit()

print("Okay! Let's Play :)")

score = 0
answer = input("What does CPU stnad for? ")
if answer.lower() == "central processing unit":
    print('Correct!')
    score += 1
else:
    print("Incorrect")

answer = input("What does GPU stnad for? ")
if answer.lower() == "graphics processing unit":
    print('Correct!')
    score += 1
else:
    print("Incorrect")

answer = input("What does RAM stnad for? ")
if answer.lower() == "random access memory":
    print('Correct!')
    score += 1
else:
    print("Incorrect")

answer = input("What does PSU stnad for? ")
if answer.lower() == "power supply unit":
    print('Correct!')
    score += 1
else:
    print("Incorrect")

print("You got " + str(score) + "/4 questions correct!")
print("You got " + str(score/4 * 100) + "% marks!")
