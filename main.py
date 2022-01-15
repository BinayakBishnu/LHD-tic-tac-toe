import store_results
import playing_board
number_board = playing_board.load_board()

player1 = input('Enter player1 name: ')
player2 = input('Enter player2 name: ')
winner = 'a'

player = player1
print('{} goes first'.format(player1))

flag = 0
while flag == 0:
    row, column = input("Enter your choice {}: ".format(player)).split()
    row = int(row)
    column = int(column)
    if player == player1:
        number_board[row-1][column-1] = 'X'
        player = player2

    elif player == player2:
        number_board[row-1][column-1] = 'Y'
        player = player1

    for row in number_board:
        print('|'.join(row))

    for row in number_board:
        if ''.join(row) == 'XXX':
            print("\nGame over\nX wins")
            winner = player1
            flag = 1

        if ''.join(row) == 'YYY':
            print("\nGame over\nY wins")
            winner = player2
            flag = 1

    s = ""
    for i in range(3):
        for j in range(3):
            if i == j:
                s += number_board[i][j]

    if s == 'XXX':
        print("\nGame over\n{} wins".format(player1))
        winner = player1
        flag = 1

    if s == 'YYY':
        print("\nGame over\n{} wins".format(player2))
        winner = player2
        flag = 1

    for j in range(3):
        s = ""
        for i in range(3):
            s += number_board[i][j]

        if s == 'XXX':
            print("\nGame over\n{} wins".format(player1))
            winner = player1
            flag = 1

        if s == 'YYY':
            print("\nGame over\n{} wins".format(player2))
            winner = player2
            flag = 1

    c = 3
    for row in number_board:
        if " " not in ''.join(row):
            c -= 1
    if c == 0:
        print("\nGame over\nDraw")
        flag = 1


print('Final board:')
for row in number_board:
    print('|'.join(row))


store_results.store(player1, player2, winner)
