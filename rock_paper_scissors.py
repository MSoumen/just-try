import random
# create items
# prompt choose
# machine choose randomly
# checking who is great
# Who Win
# if tie repeat prompt
# maka a count to make a scoreboard

#--------Global _varibles------------
item=['Rock','Paper','Scissors']
prompt=''
machine_prompt=''
win_count=0
lose_count=0

# main funtion goes here-----
def main():
    print()
    print('--------------------------------------------------------')
    print('\tRock\t' + '\tPaper\t' + '\tScissors')
    print('--------------------------------------------------------')
    print()
    prompt=input(' Enter "R" for Rock, "P" for Paper, "S" for Scissors : ')
    machine_prompt=random.choice(item)
    print('Machine Choose : ' + machine_prompt)    
    checking(prompt,machine_prompt)

# Checking...
def checking(prompt,machine_prompt):

    if (machine_prompt=='Rock'):
        if(prompt=='R' or prompt=='r'):
            tie()
        elif (prompt=='P' or prompt=='p'):
            win()
        else:
            lost()
    elif (machine_prompt=='Paper'):
        if(prompt=='R' or prompt=='r'):
            lost()
        elif (prompt=='P' or prompt=='p'):
            tie()
        else:
            win()
    else:
        if(prompt=='R' or prompt=='r'):
            win()
        elif (prompt=='P' or prompt=='p'):
            lost()
        else:
            tie()


# Winning_Function
def win():
    global win_count
    win_count+=1
    print('Wow, You Won')


# Losing_function
def lost():
    global lose_count
    lose_count+=1
    print('Blah, You Beated')

# Its_a_tie
def tie():
    print('Its a Tie')

# gaming_function
def game():
    while True:
        main()
        again=input('Play Again (Y/N) : ')[0]
        if (again!='Y' and again!='y'):
            print('You won ',win_count,' times')
            print('You lose ',lose_count,' times')
            print('Good Bye')
            break


# Main game program goes here-------
game()
