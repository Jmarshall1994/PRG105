import random

answers = ["Of course", "No", "I don't think so", "Maybe", "Doubt it", "Duh", "Yes", "Yes you will", "Perhaps", "Very unlikely", "Nope", "No way", "Absalutly", "Very likely", "You wish"]
question = 'What is your question? '

name=raw_input('What is your name : ')
print ("Hi %s! I am fortune teller Steve." % name)

def prompt_question(question):
    response = raw_input(question)
    print random.choice(answers)


prompt_question(question)

def ask_again():
    response2 = raw_input('Do you Have another question? ')
    if response2 == 'Yes' or 'yes' or 'Y':
         print prompt_question(question)
    elif response2 == 'No' or response2 == 'no':
        print "goodbye"
    else:
        print 'You need to say yes or no'


ask_again()
