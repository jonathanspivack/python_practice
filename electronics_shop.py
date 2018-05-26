# https://www.hackerrank.com/challenges/electronics-shop/problem

# with itertools
from itertools import product

def getMoneySpent(keyboards, drives, b):
    
    prod = list(product(keyboards,drives))
    prods = [x[0]+x[1] for x in prod if x[0]+x[1] <= b]    
    if len(prods) == 0:
        return -1
    
    return max(prods)
   
  
  # without itertools
  
  def getMoneySpent(keyboards, drives, b):
    keyboards = sorted(keyboards)
    drives = sorted(drives)
    maxp = -1
    
    for i in range(len(keyboards)):
        for j in range(len(drives)):
            cur = keyboards[i] + drives[j]
            if cur > b:
                break
            else:
                if cur > maxp:
                    maxp = cur
                    
    return maxp
