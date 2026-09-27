import random
comp=(random.randint(1,100))
trise=0

while True:
    trise +=1
    hum=int(input("guess a number between 1-100 -:"))

    if comp==hum:
        print(f"congratulations you win! in {trise} trise")
        break

    elif hum>comp:
        print("sorry wrong guess go lower ")

    elif hum<comp:
        print("sorry wrong guess go higher ")