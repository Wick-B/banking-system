# ADD FUNCTIONS FOR NEXT TIME
# MAKE THE PROGRAM REMEMBER THE LAST LOGGED-IN USER (ASK GPT FOR THIS LIKE YOU TOLD IT YOU WOULD)
# ADD DESIGN FEATURES

# dictionary for storing usernames and balance
users = {}

# flag for while loop
running = True

while running:
    enter_again = False

    user_name = input('Enter your name: ')

    # stores username info in users dictionary automatically if name isnt there
    if user_name not in users:
        users[user_name] = 0

    # menu of options
    print('1. Deposit')
    print('2. Withdraw')
    print('3. Check Balance')
    print('4. Switch user')
    print('5. Quit')

    # loop that handles the users banking menu
    while True:
        try:
            option = int(input('Choose an option: '))

        # adds money to balance
            if option == 1:
                while True:
                    try:
                        if enter_again:
                            enter_again = False

                        deposit = float(input('Enter deposit: '))
                        users[user_name] += deposit
                        break

                    except ValueError:
                        print('Please enter numbers only')
                        enter_again = True

        # subtracts money from balance
            elif option == 2:
                while True:
                    try:
                        if enter_again:
                            enter_again = False

                        withdrawal = float(input('Enter withdrawal: '))

                        if users[user_name] != 0:
                            users[user_name] -= withdrawal
                        else:
                            print('Error. No money to withdraw.')
                        break

                    except ValueError:
                        print('Please enter numbers only')
                        enter_again = True

        # allows user to check balance
            elif option == 3:
                print(f'Your balance: ${users[user_name]:.2f}')

        # breaks inner while loop, allowing program to ask for the username again
            elif option == 4:
                break

        # stops the whole program from running
            elif option == 5:
                print('Bye.')
                running = False
                break

        # prevents someone from typing number thats not in menu
            else:
                print('Please enter only one of the numbers 1-5.')

        # prevents error if user types in something thats not an int
        except ValueError:
            print('Please enter one of the numbers 1-5.')
