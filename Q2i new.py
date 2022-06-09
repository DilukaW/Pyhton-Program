# declaring a function to find the number of possibilities
# parameters-
# number of dice, number of sides, expected sum

# when dice count =0, and sum=0
# return 1
# execute when target sum met

# when dice count=0 ,or sum<0
# return 0
# execute when the sum is less than the target sum

def find_num_possibilities(num_dice, target_sum):
    if (num_dice == 0 and target_sum == 0):
        return 1

    elif (num_dice == 0 or target_sum <= 0):
        return 0
    else:
        # declaring a counter variable to track the number of possibilities
        sum_counter = 0
        # looping over each possibility
        for x in range(1, 7):
            # recursive approach
            sum_counter += find_num_possibilities(num_dice - 1, target_sum - x)

    return sum_counter


# declaring a function to find the total possible combinations of a dice
# parameters-
# number of dice, number of sides

# 10 dice with 6 sides
# total combinations = 6^10

def total_combinations(num_of_dice):
    # return total combinations
    return pow(6, num_of_dice)


# declaring a function to find the probability
# parameters-
# total number of items in a sample space n(s),total number of items a the event n(e)
# p=n(e)/n(s)

def find_probability(num_of_possibilities, total_outcomes):
    # return probability
    # print(num_of_possibilities)
    # print(total_outcomes)
    # print(float(float(num_of_possibilities) / total_outcomes))
    return (float(float(num_of_possibilities) / total_outcomes))


if __name__ == '__main__':
    print('CALCULATING PROBABILITY OF DICE')
    print('-------------------------------' + '\n\n')

    dice_count = int(input('Enter number of dice  : '))
    expect_sum = int(input('Enter expected sum    : '))

    combinations = (total_combinations(dice_count))
    possibilities = (find_num_possibilities(dice_count, expect_sum))
    print("possibilities" + str(possibilities))
    result = find_probability(possibilities, combinations)

    print('\nTotal number of possible combinations : ' + str(combinations))
    print('All possible ways of making {} from {} dice : {}'.format(expect_sum, dice_count, str(possibilities)))
    print('The probability that {} dice throws add up exactly to {} : {}'.format(dice_count, expect_sum,
                                                                                 str(result)) + '\n\n')
