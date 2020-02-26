import timeit
import numpy as np


charlie_ang_setup = '''
from __main__ import charlie_ang_day28
'''

def calc_position(cards,n,cache):
    key = str(n) + ":" + ",".join(str(cards))
    value = cache.get(key)
    if value is None:
        multiplier = 2**n
        if len(cards) == 1:
            # print("{}-{} ending {}".format(n,len(cards), cards))
            value = cards[0]*multiplier
        else:
            # print("{}-{} starting {} left {} right {}".format(n,len(cards), cards, cards[1:], cards[0:-1]))
            left = cards[0]*multiplier + calc_position(cards[1:], n+1, cache)
            right = cards[-1]*multiplier + calc_position(cards[0:-1], n+1, cache)
            value =  max(left, right)
        cache[key] = value
    return value

def charlie_ang_day28(cards):
    # print(len(cards))
    return calc_position(cards, 1, dict())

TEST_CODE_charlie_ang = '''
result = charlie_ang_day28([4, 10, 2, 3, 1, 3, 1, 6, 9])
'''

Kurt_Hinderer_setup = '''
from __main__ import Kurt_Hinderer_day28
'''

def Kurt_Hinderer_day28(cards):
  n = len(cards)
  table = [[0 for i in range(n)] for j in range(n)]
  for i in range(n):
      table[0][i] = 2*cards[i]
  for i in range(1,n):
      for j in range(n-i):
          left = table[i-1][j]
          right = table[i-1][j+1]
          table[i][j] = max(left*2+table[0][i+j], right*2+table[0][j])
  return table[n-1][0]

TEST_CODE_Kurt_Hinderer = '''
result = Kurt_Hinderer_day28([4, 10, 2, 3, 1, 3, 1, 6, 9])
'''

Oleksandra_Chmel_setup = '''
from __main__ import Oleksandra_Chmel_day28
'''

def Oleksandra_Chmel_day28(cards):
    length = len(cards)
    if length == 1: return cards[0] * 2
    arr = np.zeros((length,length))
    for i,e in enumerate(arr[0]):
        arr[0][i] = cards[i] * 2
    for ind,row in enumerate(arr[1:]):
        length -= 1
        for num in range(length):
            arr[ind+1][num] = max(2*arr[ind][num]+arr[0][ind+num+1], 2*arr[ind][num+1]+arr[0][num])
    return arr.max() 

TEST_CODE_Oleksandra_Chmel = '''
result = Oleksandra_Chmel_day28([4, 10, 2, 3, 1, 3, 1, 6, 9])
'''

Tushar_Jain_setup = '''
from __main__ import Tushar_Jain_day28
'''

def optimum(cards, start, last, iteration, table):
    if(table[start][last] == -1):
        if(start >= last):
            table[start][last] = cards[start]
        else:
            value1 = (cards[start] + 
                     optimum(cards, start + 1, last, 0, table) * 2)
            value2 = (cards[last] +
                     optimum(cards, start, last - 1, 0, table) * 2)
            table[start][last] = max(value1, value2)
    return table[start][last] * (2 ** iteration)

def Tushar_Jain_day28(cards):
    length = len(cards)
    table = []
    for i in range(length):
        table.append([-1 for j in range(length)])
    return optimum(cards, 0, length - 1, 1, table);

TEST_CODE_Tushar_Jain = '''
result = Tushar_Jain_day28([4, 10, 2, 3, 1, 3, 1, 6, 9])
'''

print("Time for charlie_ang test code: " + str(timeit.timeit(stmt=TEST_CODE_charlie_ang, setup=charlie_ang_setup, number=10000)) + " seconds")
print("Time for Kurt_Hinderer test code: " + str(timeit.timeit(stmt=TEST_CODE_Kurt_Hinderer, setup=Kurt_Hinderer_setup, number=10000)) + " seconds")
print("Time for Oleksandra_Chmel test code: " + str(timeit.timeit(stmt=TEST_CODE_Oleksandra_Chmel, setup=Oleksandra_Chmel_setup, number=10000)) + " seconds")
print("Time for Tushar_Jain test code: " + str(timeit.timeit(stmt=TEST_CODE_Tushar_Jain, setup=Tushar_Jain_setup, number=10000)) + " seconds")
