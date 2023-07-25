print("Welcome to my cat quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Oki! Let's play ")
score = 0

answer = input("Are cats the only mammals who cannot taste sweetness? ")
if answer.lower() == "yes":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("Finish the sentence: 'Cats can jump up to ... their lenght' ")
if answer.lower() == "six times":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("How many bones does a cat have? ")
if answer.lower() == "230":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("Do cats have whiskers on the back of their front legs? ")
if answer.lower() == "yes":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("Can a cats tongue lick a bone clean of any shred of meat? ")
if answer.lower() == "yes":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("How many toes do cats have? ")
if answer.lower() == "18":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("is the statement true?: 'Cats have the largest eyes relative to their head size of any mammal' ")
if answer.lower() == "yes":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("Which part of the cats body is most used to balanced themselves when jumping or walking along narrow ledges? ")
if answer.lower() == "tail":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

print("You got " + str(score) + " questions correct!")
print("You got " + str((score / 8) * 100) + "%.")

