import random 

choise=["rock","paper","scissors"]
tries=0

while True:
    tries +=1

    user=input('"choose"-:rock/paper/scissors -:')
    bot=random.choice(choise)

    print(f'user chose-:"{user}"')
    print(f'bot choose-:"{bot}"')

    if user==bot:
        print("match draw!")

    elif user=="rock" and bot=="scissors":
        print(f"you win in {tries} triese!")
        break

    elif user=="scissors" and bot=="paper":
        print(f"you win in {tries} tries!")
        break

    elif user=="paper" and bot=="rock":
        print(f"you win in {tries} triese!")
        break

    elif user in choise:
        print("you loose!")

    else:
        print("invalid input")

print("game over!")