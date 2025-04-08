import random
print("Welcom to the Rock,Papper,Secissors Game!")

choices = [ "rock","papper", "secissor"]
user_score = computer_score =0
print("Let\'s play!")

while True:
    user_input = input("Type Rock,Papper, Secissor or Q to quit: ").lower()
    if user_input == "q":
        print(f'Final score - you: {user_score}, computer: {computer_score}')
        print("Thanks for plaing!")
        break
    if user_input  not in choices:
        print("Invalid input , pleaase try again.")
        continue
    computer_chose = random.choice(choices)
    print(f'Computer choice: {computer_chose}.')
    if user_input == computer_chose:
        print("It's a tie!")
    elif (user_input == "rock" and computer_chose == "scisser") or \
           (user_input == "papper" and computer_chose == "rock") or \
           (user_input == "scisser" and computer_chose == "papper"):
        print("Yoy win!")
        user_score += 1

    else:
        print("Computer wins! ")
        computer_score += 1

    print(f'Current score - you: {user_score}\ncomputer: {computer_score}')        
           
        

           