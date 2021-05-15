# Problem: https://www.hackerrank.com/challenges/30-operators/problem
# Score: 30.0


import math
import os
import random
import re
import sys


def solve(meal_cost, tip_percent, tax_percent):
    tip = tip_percent * meal_cost / 100
    tax = tax_percent * meal_cost / 100
    total_cost = meal_cost + tip + tax
    
    print(round(total_cost))


meal_cost = float(input())
tip_percent = int(input())
tax_percent = int(input())
solve(meal_cost, tip_percent, tax_percent)
