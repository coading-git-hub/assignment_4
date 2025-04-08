import random
print("Welcom to the Number Guessing Game! ")

low = 1
high = 10

print("THink of a number betwee 1 to 10 and computer will be guess the number!")

if low <= high:
    guess = random.randint(low,high)
    print("Computer's guess number is: ", guess)

    while True:
        feedback = input("Is the guess too high (H), too low (L), or correct (c)".strip().upper())

        if feedback == 'C':
            print("Yah! The computer guessed your number")
            break
        elif feedback == "H":
            high = guess -1
            guess = random.randint(low,high)
            print("Computer's guess is: ",guess)
        elif feedback == "L":
            low = guess + 1
            guess =random.randint(low,high)
            print("Computer's guess is:  ", guess)
        else:
            ("Invalid input. Please enter H, L, or C.")

if low > high:
    print("The number is not in the range. Please try again.")



            


            