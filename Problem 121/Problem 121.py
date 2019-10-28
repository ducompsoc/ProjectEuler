from fractions import Fraction
from math import ceil

def prob_of_win(discs, last_probability, blues_selected, n):
    #Chance of blue is 1 / discs
    #Multiply by the last probabilty as events are independent as we replace

    #Taken n discs out
    if discs == n + 1:
        #They have won if over half are blue
        if blues_selected > n // 2:
            return last_probability

        #Otherwise this branch was a loss
        return 0

    #Put another disc in
    discs += 1

    #Pick a blue
    blues_selected += 1
    #P(blue) = 1 / discs
    blue_last = last_probability * Fraction(1, discs)

    #Pick a red, P(red) = (discs - 1) / discs
    red_last = last_probability * Fraction(discs - 1, discs)

    #Recursively calculate the probability of winning until they reach the maximum number of discs
    return prob_of_win(discs, blue_last, blues_selected, n) + prob_of_win(discs, red_last, blues_selected - 1, n)

def solve(turns):
    prob = prob_of_win(1, 1, 0, turns)
    #P(wins) = 1/x then x = expected number of times to play before winning
    #So 1/P(wins) = x so x - 1 is should be the maximum prize pool to at least break even
    print("After", turns, "turns, the chance of winning is:", prob, "which is", round(float(prob * 100), 4), "%")
    print("The maximum prize fund should be: £", ceil(prob ** -1) - 1, sep = '')

solve(15)
    
