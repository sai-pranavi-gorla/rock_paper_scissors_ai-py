import random

print("AI Based Rock Paper Scissors Game")
print("Type rock, paper, or scissors")
print("Type 'exit' to stop the game\n")

user_score = 0
computer_score = 0

choices = ["rock", "paper", "scissors"]

while True:
    user = input("Enter your choice: ").lower()

    if user == "exit":
        print("\nGame Over")
        print("Final Score -> You:", user_score, " Computer:", computer_score)
        break

    if user not in choices:
        print("Invalid choice! Try again.\n")
        continue

    computer = random.choice(choices)
    print("Computer chose:", computer)

    if user == computer:
        print("Result: It's a Tie!")
    
    elif (user == "rock" and computer == "scissors") or \
         (user == "paper" and computer == "rock") or \
         (user == "scissors" and computer == "paper"):
        print("Result: You Win!")
        user_score += 1

    else:
        print("Result: Computer Wins!")
        computer_score += 1

    print("Score -> You:", user_score, " Computer:", computer_score)
    print("-" * 30)
