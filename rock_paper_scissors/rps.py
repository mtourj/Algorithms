#!/usr/bin/python

# Given n, return all possible permutations of n plays

# Example:
'''
1.
[['rock'], ['paper'], ['scissors']]

2.[['rock', 'rock'], ['rock', 'paper'], ['rock', 'scissors'],
  ['paper', 'rock'], ['paper', 'paper'], ['paper', 'scissors'],
  ['scissors', 'rock'], ['scissors', 'paper'], ['scissors', 'scissors']]

'''

import sys


cache = {
  0: [[]],
  1: [['rock'], ['paper'], ['scissors']]
}

def rock_paper_scissors(n):
    plays = []

    if n in cache:
        return cache[n]
    else:
        for play in rock_paper_scissors(n - 1):
            for valid_play in cache[1]:
                plays.append(play + valid_play)

    cache[n] = plays

    return cache[n]


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_plays = int(sys.argv[1])
        print(rock_paper_scissors(num_plays))
    else:
        print('Usage: rps.py [num_plays]')
