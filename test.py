from matplotlib import pyplot as plt
import numpy as np
import json

with open('train.json') as json_data:
    d = json.load(json_data)

def print_im(data, n, b):
    band = data[n]['band_' + str(b)]
    img = np.zeros(shape=(75,75))
    r = range(75)
    r = [x * 75 for x in r]
    for i in r:
        img[i//75,0:75] = band[i:i+75]

    plt.imshow(img)
    plt.show(block=False)

def fasit(data,n):
    return(str(data[n]['is_iceberg']))

def inc_angle(data,n):
    print('Inc angle: ' + str(data[n]['inc_angle']))


def competition():
    p1 = input('Player 1 - is iceberg?  (0/1): ')
    p2 = input('Player 2 - is iceberg?  (0/1): ')
    return([p1, p2])

def main():
    n = 3

    pointsPlayer1 = 0
    pointsPlayer2 = 0
    while True:
        n+=1
        inc_angle(d,n)
        print_im(d,n,1)
        plt.show()

        print()
        answers  = competition()
        icebergOrShip = fasit(d,n)

        print('SOLUTION:  Is iceberg: ' + icebergOrShip)

        if (answers[0] == icebergOrShip and answers[1] == icebergOrShip):
            print('Both are correct!')
            pointsPlayer1 += 1
            pointsPlayer2 += 1
        elif (answers[0] == icebergOrShip and answers[1] != icebergOrShip):
            print('Player 1 is correct')
            pointsPlayer1 += 1
        elif (answers[0] != icebergOrShip and answers[1] == icebergOrShip):
            print('Player 2 is correct')
            pointsPlayer2 += 1
        else:
            print('None are right.')
        print()

        print('Player 1: ', pointsPlayer1)
        print('Player 2: ', pointsPlayer2)

        while True:
            i = input('Continue? (y/n): ')

            if i.lower() == 'y':
                print()
                print('---------------------------------------------')
                print()
                break
            elif i.lower() == 'n':
                print()
                if (pointsPlayer1 > pointsPlayer2):
                    print('************ Player 1 wins! ************')
                elif (pointsPlayer2 > pointsPlayer1):
                    print('************ Player 2 wins! ************')
                else:
                    print("************ It's a draw! ************")
                return


main()
