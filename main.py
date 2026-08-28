import random

# Try for pencils total
while True: 
    try: 
        pencils_total = int(input('How many pencils would you like to use:'))
    except ValueError:
        print("The number of pencils should be numeric")
    else: 
        if pencils_total < 0:
            print("The number of pencils should be numeric")
        else:
            if pencils_total == 0:
                print('The number of pencils should be positive')
            else:
                break

# Choosing the player
while True: 
    first_player = input('Who will be the first (John, Jack):')
    second_player = "0"

    if first_player == 'John':
        second_player = 'Jack'
        break

    elif first_player == 'Jack':
        second_player = 'John'
        break

    else: 
        print('Choose between John and Jack')


print(f"{pencils_total * '|'}")

# Player can take 1,2,3 and too many pencils 

while pencils_total > 0:

    while True:
        if first_player == 'Jack':  # bot's logic
            print(f"{first_player}'s turn:")
            
            if pencils_total == 1:
                first_player_decision = 1
            elif pencils_total % 4 == 0:
                first_player_decision = 3
            elif pencils_total % 4 == 3:
                first_player_decision = 2
            elif pencils_total % 4 == 2:
                first_player_decision = 1
            elif pencils_total % 4 == 1:
                first_player_decision = random.randint(1, 3)

            print(first_player_decision)
            pencils_total = pencils_total - first_player_decision
            print(f"{pencils_total * '|'}")
            last_player = second_player
            break
            
        else:  # human's logic
            first_player_decision = input(f"{first_player}'s turn:")

            if first_player_decision in ['1', '2', '3']:
                if int(first_player_decision) > pencils_total:
                    print('Too many pencils were taken')
                    continue
                else:
                    pencils_total = pencils_total - int(first_player_decision)
                    print(f"{pencils_total * '|'}")
                    last_player = second_player
                    break
            else: 
                print("Possible values: '1', '2' or '3'")
                continue


    if pencils_total <= 0: 
        print(f"{last_player} won!")
        break
    else: 
        pass


    while True:
            if second_player == 'Jack':  # bot's logic
                print(f"{second_player}'s turn:")
                
                if pencils_total == 1:
                    second_player_decision = 1
                elif pencils_total % 4 == 0:
                    second_player_decision = 3
                elif pencils_total % 4 == 3:
                    second_player_decision = 2
                elif pencils_total % 4 == 2:
                    second_player_decision = 1
                elif pencils_total % 4 == 1:
                    second_player_decision = random.randint(1, 3)

                print(second_player_decision)
                pencils_total = pencils_total - second_player_decision
                print(f"{pencils_total * '|'}")
                last_player = first_player
                break
                
            else:  # human's logic
                second_player_decision = input(f"{second_player}'s turn:")

                if second_player_decision in ['1', '2', '3']:
                    if int(second_player_decision) > pencils_total:
                        print('Too many pencils were taken')
                        continue
                    else:
                        pencils_total = pencils_total - int(second_player_decision)
                        print(f"{pencils_total * '|'}")
                        last_player = first_player
                        break
                else: 
                    print("Possible values: '1', '2' or '3'")
                    continue


    if pencils_total <= 0: 
        print(f"{last_player} won!")
        break
    else: 
        pass