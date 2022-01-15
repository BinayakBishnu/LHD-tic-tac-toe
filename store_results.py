def store(player1, player2, winner):
    f = open('results.txt', 'a')

    f.write('{} vs {}\n'.format(player1, player2))
    f.write(winner + '\n_\n')
    f.close()

    f = open('players.txt', 'a')
    f.write('{} and {}\n'.format(player1, player2))
    f.close()


if __name__ == '__main__':
    print('store results file')
