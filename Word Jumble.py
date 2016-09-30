


import random

colors = ["RED", "YELLOW", "BLUE", "GREEN", "PINK", "PURPLE"]



selection = random.choice(colors)
answer = selection


jumble = list(selection)


for current_index in range(len(jumble)):
    random_index = random.randrange(0, len(jumble))
    temp = jumble[current_index]
    jumble[current_index] = jumble[random_index]
    jumble[random_index] = temp

for letter in jumble:
    print letter,


guess = raw_input("\nWhat color is jumbled?")
guess = guess.upper()

if guess == answer:
    print ("Got It")
else:
    print (answer)