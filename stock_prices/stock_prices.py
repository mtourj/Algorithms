#!/usr/bin/python

import argparse

def find_max_profit(prices):

  min_price, max_price = 0, 1

  # Max starts at 1 because the sell
  # must happen AFTER the buy
  # Eliminating possbility of happening
  # at the 'same time'
  for i in range(1, len(prices)):
    if prices[i] > prices[max_price]:
      max_price = i

  for i in range(max_price):
    if(prices[i] < prices[min_price]):
      min_price = i

  return prices[max_price] - prices[min_price]

  


if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))