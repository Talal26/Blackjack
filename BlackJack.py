import time

ace_player = False
ace_dealer = False

cards = {'AC', '2C', '3C', '4C', '5C', '6C', '7C', '8C', '9C', '10C', 'JC', 'QC', 'KC', 'AD', '2D', '3D', '4D', '5D',
         '6D', '7D', '8D', '9D', '10D', 'JD', 'QD', 'KD', 'AH', '2H', '3H', '4H', '5H', '6H', '7H', '8H', '9H', '10H',
         'JH', 'QH', 'KH', 'AS', '2S', '3S', '4S', '5S', '6S', '7S', '8S', '9S', '10S', 'JS', 'QS', 'KS'}

values = {'A': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '1': 10, 'J': 10, 'Q': 10, 'K': 10}

player = []
dealer = []

player.append(cards.pop())
dealer.append(cards.pop())
player.append(cards.pop())
dealer.append(cards.pop())

player_str = ', '.join(player)
dealer_str = ', '.join(dealer)

print(f'You have {player_str}')
print(f'The dealer has a {dealer[0]}')

sum_player = values[player[0][0]] + values[player[1][0]]
sum_dealer = values[dealer[0][0]] + values[dealer[1][0]]

if player[0][0] == 'A' or player[1][0] == 'A':
    ace_player = True

if dealer[0][0] == 'A' or dealer[1][0] == 'A':
    ace_dealer = True

if ace_player:
    print(f'Your current total is: {sum_player} or {sum_player + 10}')
else:
    print(f'Your current total is: {sum_player}')

while True:
    choice = input('Hit or Stand? ').lower()
    if len(choice) == 0:
        print('Please type a valid input')
    elif choice.startswith('h'):
        player.append(cards.pop())
        player_str = ', '.join(player)
        sum_player += values[player[-1][0]]
        if player[-1][0] == 'A':
            ace_player = True
        print(f'You have {player_str}')
        if ace_player and sum_player < 12:
            print(f'Your current total is: {sum_player} or {sum_player + 10}')
        else:
            ace_player = False
            print(f'Your current total is: {sum_player}')
        if sum_player >= 21:
            break
    elif choice.startswith('s'):
        break
    else:
        print('Please type a valid input')

if ace_player:
    sum_player += 10
sum_dealer = values[dealer[0][0]] + values[dealer[1][0]]
if sum_player < 21:
    print(f'The dealer\'s first two cards were {dealer_str}')
    if ace_dealer:
        if sum_dealer < 7:
            if ace_dealer:
                print(f'The dealer\'s total is currently at: {sum_dealer} or {sum_dealer + 10}')
            else:
                print(f'The dealer\'s total is currently at: {sum_dealer}')
            while (sum_dealer < 7 and ace_dealer) or (sum_dealer < 17 and not ace_dealer):
                time.sleep(1)
                dealer.append(cards.pop())
                sum_dealer += values[dealer[-1][0]]
                dealer_str = ', '.join(dealer)
                print(f'The dealer has {dealer_str}')
                if 12 > sum_dealer >= 7:
                    sum_dealer += 10
                    print(f'The dealer\'s total is at: {sum_dealer}')
                elif sum_dealer >= 12:
                    ace_dealer = False
                    print(f'The dealer\'s total is currently at: {sum_dealer}')
                else:
                    print(f'The dealer\'s total is currently at: {sum_dealer} or {sum_dealer + 10}')
        elif 12 > sum_dealer >= 7:
            sum_dealer += 10
            print(f'The dealer\'s total is at: {sum_dealer}')
        elif sum_dealer >= 12:
            ace_dealer = False
            print(f'The dealer\'s total is currently at: {sum_dealer}')
    else:
        print(f'The dealer\'s total is currently at: {sum_dealer}')
        while sum_dealer < 17:
            time.sleep(1)
            dealer.append(cards.pop())
            sum_dealer += values[dealer[-1][0]]
            dealer_str = ', '.join(dealer)
            print(f'The dealer has {dealer_str}')
            if sum_dealer >= 17:
                print(f'The dealer\'s total is at: {sum_dealer}')
            else:
                print(f'The dealer\'s total is currently at: {sum_dealer}')

if sum_player > 21:
    print('You Lose')
elif sum_dealer > 21:
    time.sleep(1)
    print('You Win!')
elif sum_dealer > sum_player:
    time.sleep(1)
    print('You Lose')
elif sum_dealer == sum_player:
    time.sleep(1)
    print('It\'s a tie!')
elif sum_dealer < sum_player:
    time.sleep(1)
    print('You Win!')
