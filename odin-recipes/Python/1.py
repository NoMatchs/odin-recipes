# a = 2 + 2
# print(a)

# print((2 + 3) * 6)

# print(48565878 * 578453)

# print(2 ** 8)

# print(2 * 8)

# print(23 // 7)

# print(23 / 7)

# print(23 % 7)

# print((5-1) * ((7 + 1) / (3-1)))

# # print(4 +* 2)

# # print('jq21)

# print(4 * + 2)

# print('alice' + 'bob')


# print('Alice' * 2)

# spam = 40

# eggs = 2 + 2

# print(spam + eggs)

# spam = spam + 2

# print(spam)

# spam = 'Hello'

# print(spam)

# spam = 'Goodbye'

# print(spam)

# print('Hello' + ', World')

# print('What is your name?')

# my_name = input('>')

# print('It is good to meet you,' + my_name)
# print("The length of your name is:")
# print(len(my_name))
# print('What is your age?')
# my_age = input('>')
# print('You will be ' + str(int(my_age) + 1)  + ' in a year')

# print(type(32))

# type(43.22)

# type('forty two')

# name = 21

# type(name)

# print(round(32.19,1))

# print(round(3.50,1))

# print(round(-2.2,2))

# print((4 < 5) and (5 < 6))

# print(4 < 5) or (9 < 7)

# print(1 == 2) and (2 == 2)

# print(not(1 == 2))

# name = 'alice'

# if name == 'alice':
#     print('Hi, alice')
# else:
#     print('Hi,stranger')

# name = 'alice'
# age = 33
# if name != 'alice':
#     print('Hi,alice')
# elif age > 12:
#     print('you are not alice,kiddo.')

# today_is_opposite_day = True

# if today_is_opposite_day == True:
#     spy_it_is_opposite_day = True
# else:
#     spy_it_is_opposite_day = False

# print('Enter TB or GB for the advertised unit:')
# unit = input('>')

# if unit == "TB" or unit == 'tb':
#     discrepancy = 10000000000000 / 1099511627776
# elif unit == 'GB' or unit == 'gb':
#     discrepancy = 10000000000 / 1073741824

# print('Enter the advertises capacity:')
# advertised_capacity = input('>')
# advertised_capacity = float(advertised_capacity)

# real_capacity = str(round(advertised_capacity* discrepancy,2))

# print('The actual capacuty is ' + real_capacity + " " + unit)

# spam = 0
# while spam < 5:
#     print(spam)
#     spam += 1
# name = ''
# while name != 'your name':
#     print("Please type your name.")
#     name = input('>')
# print('Thank you!')

# print('Hello world')
# for i in range(5):
#     print("On this iteration, i is set to " + str(i))
# print("Goodbye")

# total = 0
# for i in range(101):
#     total += i
# print(total)

# import random
# for i in range(5):
#     print(random.randint(1,10))

# import sys

# while True:
#     print('Type exit to exit.')
#     response = input('>')
#     if response == 'exit':
#         sys.exit()
#     print('You typed' + response + '.')

# import random
# secret_number = random.randint(1,20)
# print('I am thinking of a number between 1 and 20.')

# for guesses_taken in range(1,7):
#     print('Take a guess.')
#     guess = int(input('>'))

#     if guess < secret_number:
#         print("Too low.")
#     elif guess > secret_number:
#         print('Too high')
#     else:
#         break
# if guess == secret_number:
#     print("Good job! You got it in" + str(guesses_taken) + 'guesses!')
# else:
#     print('Nope. Thne number was ' + str(secret_number))\\

import random, sys

print('Rock,PAPER,SCISSORS')

wins = 0
losses = 0
ties = 0

while True:
    print('%s Wins, %s Losses, %s Ties' % (wins,losses,ties))
    while True:
        print("Rnter your move: (r)ock (p)aper (s)scissors or (q)uit")
        player_move = input('>')
        if player_move == 'q':
            sys.exit()
        if player_move =='r' or player_move == 'p' or player_move == 's':
            break
        print("Type one of r,p,s,or .")
    if player_move == 'r':
        print("ROCK versus...")
    elif player_move == 'p':
        print("PAPER versus...")
    elif player_move == "s":
        print("SCCISSORS versus...")

    move_number = random.randint(1,3)
    if move_number == 1:
        computer_move = 'r'
        print("ROCK")
    elif move_number == 2:
        computer_move = 'p'
        print("PAPER")
    elif move_number == 3:
        computer_move = 's'
        print("SCISSORS")

    if player_move == computer_move:
        print('it is a tie!')
        ties += 1
    elif player_move == 'r' and computer_move == 's':
        print("You win!")
        wins += 1
    elif player_move == 'r' and computer_move == 'p':
        print('You lose!')
        losses += 1
    elif player_move == 's' and computer_move == 'p':
        print("You win!")
        wins += 1
    elif player_move == 's' and computer_move == 'r':
        print('You lose!')
        losses += 1
    elif player_move == 'p' and computer_move == 'r':
        print("You win!")
        wins += 1
    elif player_move == 'p' and computer_move == 's':
        print('You lose!')
        losses += 1

    print('Tie:' + str(ties) + ' Win:' + str(wins) + ' Lose:' + str(losses))
