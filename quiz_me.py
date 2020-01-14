
def quiz():
    ''' creates one question with choices and an answer. 
    '''
    questions = []

    title = input("What's the title of this")
    any_more = 'Y'
    while any_more == 'Y':
        number = 0
        while any_more == ('Y'):
                number += 1
                question = input("What's the question?")
                choice1 = input("Option 1: ")
                choice2 = input("Option 2: ")
                choice3 = input("Option 3: ")
                choice4 = input("Option 4: ")
                correct = input("Which is correct?")
                questions.append([number, question, choice1, choice2, choice3, choice4, correct])
                any_more = (input("Any more questions? Y/N"))
    
    print(title)
    print(questions)
    return 

quiz()