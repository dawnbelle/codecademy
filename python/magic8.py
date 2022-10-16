import random

name = input('Enter your name: ')
question = input('Enter your question: ')
answer = ''

random_number = random.randint(1, 9)
# print(random_number)

if random_number == 1:
    answer = 'Yes - most certainly.'
elif random_number == 2:
    answer = 'It is decidedly so.'
elif random_number == 3:
    answer = 'My sources say no.'
elif random_number == 4:
    answer = 'Very doubtful.'
elif random_number == 5:
    answer = 'Better not tell you now.'
elif random_number == 6:
    answer = 'Concentrate and ask again.'
elif random_number == 7:
    answer = 'Outlook is good.'
elif random_number == 8:
    answer = 'As I see it, yes.'
elif random_number == 9:
    answer = 'Dont count on it.'
else: 
    answer = 'Error'

if name == '' or question == '':
    print('You must provide the requested details, or I can not help you')
else:
    print('Magic 8-Balls answer: ' + answer)

