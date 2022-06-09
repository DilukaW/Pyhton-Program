# In a three-person duel,players A, B and C have accuracies
# (probabilities of hitting on a single shot) of 5/6, 4/6 and 2/6.
# Have each player ﬁre at the most accurate (surviving) opponent.
# Estimate the probabilities of A, B and C surviving by simulating 1000 duels.
#
# Accuracy of 'A' = 0.833
# Accuracy of 'B' = 0.667
# Accuracy of 'C' = 0.333
#
# A = player 0
# B = player 1
# C = player 2
#
#
#

def DuelTest():
    # ---------------------------------------------------------------------------------------------------------
    #
    ## DUEL_TEST tests DUEL_SIMULATION.

    import numpy as np

    print('')
    print('DUEL_TEST:')
    print('  DUEL_SIMULATION repeatedly iterates the "duel" between the three combatants,')
    print('  who fire alternately at each other, with known probabilities')
    print('  of hitting each other.')
    # -----------------------------------------------------------------------------------------
    # inserting the accuracy probabilities of the players
    prob = np.array([0.833, 0.667, 0.333])

    # number of duels to be fought
    print('')
    Rounds = int(input('Enter the number of Rounds:'))

    print('')
    print('  In this example, the one shot probabilities are:')
    print('  Player[0]: %g' % (prob[0]))
    print('  Player[1]: %g' % (prob[1]))
    print('  Player[2]: %g' % (prob[2]))
    print('')
    print('  The number of duels to fight is %d' % (Rounds))

    # calling the DuelSimulation
    # getting the probabilties of each players into pCounter
    # average turns it took for on round into TurnAvg
    pCounter, TurnAvg = DuelSimulation(prob, Rounds)

    print('')
    print('  Result of the duels:')
    for player in range(0, 3):
        print('  Player %d winning probability is %g' % (player, pCounter[player]))

    print('')
    print('  The average number of shots fired was %g' % (TurnAvg))
    print('')
    return


def DuelSimulation(prob, Rounds):
    # --------------------------------------------------------------------------------------------
    # DuelSimulation: calls duel_once, records the survivors
    # records the times each player win and calculate the probability of winning of
    # each player. also it counts the number of rounds it takes each iteration and
    # takes the average amount of rounds
    import numpy as np

    # initializing an empty array
    pCounter = np.zeros(3)
    # setting the turn average counter for each round to zero
    TurnAvg = 0

    for duel in range(0, Rounds):
        # taking the survivor and the number of turns from duel_once
        survivor, turn_num = duel_once(prob)
        # number of times win by a player
        pCounter[survivor] = pCounter[survivor] + 1
        TurnAvg = TurnAvg + turn_num

    # calculating the Averages:   avg of x = x/n(x)
    pCounter = pCounter / float(Rounds)
    TurnAvg = TurnAvg / float(Rounds)

    return pCounter, TurnAvg


def duel_once(prob):
    # --------------------------------------------------------------------------------------------
    # duel_once executes one cycle of the duel

    import numpy as np
    # turn of shooting =0
    turn_num = 0

    while (True):
        #
        #  A fires.
        #
        turn_num = turn_num + 1
        # generating a value 1 - 10^-8
        r = np.random.rand(1)
        if (r[0] <= prob[0]):
            # if A do not miss he will shoot B,
            # A and C wil be left
            shooter = 0
            leftAlone = 2
            break

        #
        #  B fires.
        #
        turn_num = turn_num + 1
        r = np.random.rand(1)
        if (r[0] <= prob[1]):
            shooter = 1
            leftAlone = 2
            break

    survivor, turn_num = duel_twice(prob, shooter, leftAlone, turn_num)
    return survivor, turn_num

def duel_twice(prob, shooter, leftAlone, turn_num):
    # --------------------------------------------------------------------------------------------

    import numpy as np

    while (True):
        #
        #  Player who was left Alone fires.
        #
        turn_num = turn_num + 1
        r = np.random.rand(1)
        if (r[0] <= prob[leftAlone]):
            survivor = leftAlone
            break

        shooter = shooter + leftAlone
        leftAlone = shooter - leftAlone
        shooter = shooter - leftAlone

    return survivor, turn_num


def timestamp():
    # --------------------------------------------------------------------------------------------

    import time

    t = time.time()
    print(time.ctime(t))

    return None


if __name__ == '__main__':
    timestamp()
    DuelTest()
    timestamp()
