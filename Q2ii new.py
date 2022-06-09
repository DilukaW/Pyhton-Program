import random

# declaring a function to simulate the dice
# parameters-
# throwing count, target sum 

def simulate(times,t_sum):
    
    # a variable to count the number of times getting the expected sum  
    sum_count=0
    # looping the throws
    for x in range(times):
        # generating random numbers for 10 dice
        d1=random.randint(1,6)
        d2=random.randint(1,6)
        d3=random.randint(1,6)
        d4=random.randint(1,6)
        d5=random.randint(1,6)
        d6=random.randint(1,6)
        d7=random.randint(1,6)
        d8=random.randint(1,6)
        d9=random.randint(1,6)
        d10=random.randint(1,6)
        # adding the values of dice
        dice_total=d1+d2+d3+d4+d5+d6+d7+d8+d9+d10
        
        if dice_total==t_sum:
           # count increment by 1 if the total is equal to the expected sum
           sum_count+=1
    
    return sum_count



def find_probability(num_of_possibilities,total_outcomes):
    # return probability
    return num_of_possibilities/total_outcomes



if __name__=='__main__':

    print('DICE SIMULATION')
    print('---------------'+'\n\n')

    times=int(input('Enter the expected times to simulate : '))
    simulate_sum=int(input('Enter the expected simulate sum : '))

    print('\nThe number of times the results add up to {} by simulating {} times : {}'.format(simulate_sum,times,str(simulate(times,simulate_sum))))
    print('The probability of the results add up to {} by simulating {} times  : {}'.format(simulate_sum,times,str(find_probability(simulate(times,simulate_sum),times))))

