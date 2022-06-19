def isEven(n):
    """
    Daniel
    """
    return n % 2 == 0

  
def isEven(n):
    """
    the cooler Daniel
    """
    if n % 2 == 0:
        return True
    else:
        return False

      
def isEven(n):
    """
    you said i must use modulo?
    credit to: u/spaceghostuu
    """
    return n % 10 in (0, 2, 4, 6, 8)


def isEven(n):
    """
    not dumb enough to be blamed
    """
    return n/2 == int(n/2)

  
def isEven(n):
    """
    the graphic one
    """
    return int(str(n)[-1]) in (0, 2, 4, 6, 8)

  
def isEven(n):
    """
    binary variant
    """
    return bin(n)[-1] == 0

  
def isEven(n):
    """
    for whatever reason i love this one
    """
    res = [True, False]
    while True:
        try:
            return res[n]
        except IndexError:
            res.extend([True, False])

            
from itertools import cycle

def isEven(n):
    """
    this one is mine (or at least i've never seen it anywhere)
    """
    res = cycle([True, False])
    for index, value in enumerate(res):
        if index == abs(n):
            return value

          
def isEven(n):
    """
    a feeling of déjà vu
    """
    return (True, False)[n%2]

  
def isEven(n):
    """
    the very stupid one
    """
    if n == 0: return True
    if n == 1: return False
    if n == 2: return True
    if n == 3: return False
    if n == 4: return True
    if n == 5: return False
    if n == 6: return True
    if n == 7: return False
    if n == 8: return True
    if n == 9: return False
    if n == 10: return True
    if n == 11: return False
    if n == 12: return True
    if n == 13: return False
    if n == 14: return True
    if n == 15: return False
    if n == 16: return True
    if n == 17: return False
    if n == 18: return True
    ...

    
def isEven(n):
    """
    the recurcive one
    """
    if n == 0:
        return True
    elif n == 1:
        return False
    else:
        return isEven(n-2)

      
def isEven(n):
    """
    i'm not paid enough to do your work
    all credits to u/FalconBusiness4913
    """
    ans = input("Was the number you entered even ?")
    return ans == "yes":

      
def isEven(n):
    return not isOdd(n)
def isOdd(n):
    return not isEven(n)

  
def isEven(n):
    """
    i'm never wrong
    credit to: u/SnasSn
    """
    n *= 2
    return True

  
import random
random.seed(5) # TODO: find the seed who always work
def isEven(n):
    """
    i'm right!... most of the time
    credit : u/_DaCoolOne_, u/ImpressiveResponse68
    """
    return random.choice([True, False])

  
def factorial(n):
    res = 1
    for i in range(1, n+1):
        res *= i
    return res
def is_prime(n):
    return (factorial(n-1) + 1) % n == 0
def isEven(n):
    """
    i'm not even gonna make you think i understand what append here
    credit: u/allIsayislicensed
    """
    for x in range(3, n+1):
        for y in range(3, n+1):
            if is_prime(x) and is_prime(y) and x + y == n:
                    return True
    return False

def isEven(n):
  """
  I don't know map is sometimes cool
  credits: Darksorcen
  """
  return list(map(lambda x: x % 2 == 0, range(n+1)))[n]

def isEven(n):
    """
    Still using modulo !
    """
    return n//2 in [i//2 for i in range(1000) if i%2 == 0]
