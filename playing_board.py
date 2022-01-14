def load_board():
    print("Your board:\n")
    print("__|__|__\n__|__|__\n  |  |  \n")

    number_board = [[" " for i in range(j*3, (j+1)*3)] for j in range(2)]
    number_board += [[" " for i in range(j*3, (j+1)*3)] for j in range(2, 3)]

    for row in number_board:
        print('|'.join(row))

    print(number_board)


if __name__ == '__main__':
    print("board file")
