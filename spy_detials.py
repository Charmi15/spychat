# import statements
from main import spy
from start_chat import  start_chat

print "Let's get started!"
question = "Do you want to continue as " + spy['salutation'] + " " + spy['name'] + " (Y/N): "
existing = raw_input(question)

# validating users input
if (existing == 'Y' or existing == 'y') :
    # logic here.
    start_chat(spy['name'],spy['age'],spy['rating'],spy['is_online'])   #replace by dictionary
elif (existing == 'N' or existing == 'n'):
    # new users code here.
    spy['name'] = raw_input("Provide your name here :")
    # chek whether spy has input something or not
    if len(spy['name']) > 0:
        # code block if the condition is true.
        # concatination of salutation and name.
        spy['age'] = 0
        spy['rating'] = 0.0
        spy['is_online'] = False
        spy['slautation'] = raw_input("What should we all you ? : ")
        spy['age'] = raw_input("Enter your age. ?")
        print type(spy['age'])
        spy_age = int(spy['age'])
        print type(spy['age'])
        spy['name'] = spy['salutation'] + " " + spy['name']
        print 'Welcome ' + spy['name'] + " Glad to have you back with us."
        print "Alright " + spy['name'] + "i'd like know liitle bit more about you before we proceed further."
    else:
        print "Invalid name. Try again."
else:
    print "Wrong choice. Try again."
