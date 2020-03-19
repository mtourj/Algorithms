#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  
  min_batches = None

  for key in recipe.keys():
    batches_with_ingredient = ingredients.get(key)

    if(batches_with_ingredient == None):
      min_batches = 0
      break
    else:
      batches_with_ingredient //= recipe[key]
    
    if min_batches == None or min_batches > batches_with_ingredient:
      min_batches = batches_with_ingredient

  return min_batches


if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))