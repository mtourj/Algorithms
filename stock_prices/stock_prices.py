#!/usr/bin/python

import argparse

def find_max_profit(prices):

  min, max = 0, 1

  # Max starts at 1 because the sell
  # must happen AFTER the buy
  # Eliminating possbility of happening
  # at the 'same time'
  for i in range(1, len(prices)):
    if prices[i] > prices[max]:
      max = i

  for i in range(max):
    if(prices[i] < prices[min]):
      min = i

  return prices[max] - prices[min]

  


if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))