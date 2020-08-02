#winning r, p, s
# Rock vs. paper = paper
#rock vs. scissor = rock
#paper vs. scissor = scissor

#instruction
print("Enter choice r - rock, p - paper, s - scissor")
#take input
user_choice = input("User turn: ")

#computer randomly chooses any letter among r, p, s
comp_choice = random.choice(['r', 'p', 's'])

if comp_choice == user_choice:
    input("Tie! Choose new letter: ")
elif comp_choice == 'r' and user_choice == 'p':
    print("You chose paper. The computer chose rock.")
    print("YAY, you win. :)")
elif comp_choice == 'r' and user_choice == 's':
    print("You chose scissors and the computer chose rock.")
    print("Oh no, you lost :(")
elif comp_choice == 'p' and user_choice == 's':
    print("You chose scissors and the computer chose paper")
    print("Yay, you win! So smart. :)")
elif comp_choice == 'p' and user_choice == 'r':
    print("You chose rock. The computer chose paper.")
    print("YAY, you win. :)")
elif comp_choice == 's' and user_choice == 'r':
    print("You chose rock and the computer chose scissors.")
    print("YAY, you win. :)")
elif comp_choice == 's' and user_choice == 'p':
    print("You chose paper and the computer chose scissors")
    print("Oh no, you lost :(")
