import random #importing
computers_number=random.randint(1,50) #use random to choose the number
prompt='What ir your guessing?' # Prompt message 

def do_guess_round():
    computers_number=random.randint(1,50) #added
    while True:
        players_guess=input(prompt)
        if computers_number==int(players_guess):
            print("Correct! ")
            break
        elif computers_number>int(players_guess):
            print("Too Low!")
        else:
            print("Too high!")
while True:
    print("Starting a new round!")
    do_guess_round()
    print("") #blank line
