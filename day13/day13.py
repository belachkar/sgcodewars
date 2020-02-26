import timeit


akash_agarwal_setup = '''
from __main__ import akash_agarwal_day13
'''

def akash_agarwal_day13(arr):
    di={"NORTH":1, "WEST":-1j, "SOUTH":-1, "EAST":1j}
    l,t1=[],0
    for i in arr:
        if (t1+di[i]==0):
            l.pop()                     #if north-south or east-west comes one after another
            if not(len(l)):t1=0         #then pop the prev and dont add the current
            else: t1=di[l[-1]]          #update the prev element after pop element
        else:
            l.append(i)
            t1=di[i]
    return l 

TEST_CODE_akash_agarwal = '''
result = akash_agarwal_day13(["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"])
'''

akash_karan_setup = '''
from __main__ import akash_karan_day13
'''

def akash_karan_day13(arr):
    di={"NORTH":1, "WEST":-1j, "SOUTH":-1, "EAST":1j}
    l,t1=[],0
    for i in arr:
        if (t1+di[i]==0):
            l.pop()                     #if north-south or east-west comes one after another
            if not(len(l)):t1=0         #then pop the prev and dont add the current
            else: t1=di[l[-1]]          #update the prev element after pop element
        else:
            l.append(i)
            t1=di[i]
    return l 

TEST_CODE_akash_karan = '''
result = akash_karan_day13(["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"])
'''

ccquiel_setup = '''
from __main__ import ccquiel_day13
'''

def ccquiel_day13(arr):
    dirnum = {"NORTH": 1, "SOUTH": -1,
            "EAST":  2,  "WEST": -2}
    index = 0
    while index < (len(arr) - 1):
        if dirnum[arr[index]] + dirnum[arr[index+1]] == 0:
            arr = arr[:index] + arr[index+2:]
            index = 0
        else:
            index += 1
    return arr

TEST_CODE_ccquiel = '''
result = ccquiel_day13(["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"])
'''

Charlie_Ang_setup = '''
from __main__ import Charlie_Ang_day13
'''

def Charlie_Ang_day13(arr):
    opposites = { "NORTH":"SOUTH", "SOUTH":"NORTH", "EAST":"WEST", "WEST":"EAST" }
    done = False
    while not done:
        done = True
        for index in range(len(arr)-1):
            if arr[index + 1] == opposites[arr[index]]:
                arr.pop(index+1)
                arr.pop(index)
                done = False
                break
    return arr

TEST_CODE_Charlie_Ang = '''
result = Charlie_Ang_day13(["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"])
'''

diana_henninger_setup = '''
from __main__ import diana_henninger_day13
'''

def opposite(x,y):
    return (x=="NORTH" and y=="SOUTH") or (x=="SOUTH" and y=="NORTH") or (x=="WEST" and y=="EAST") or (x=="EAST" and y=="WEST")
def diana_henninger_day13(arr):
    i = 0
    while (i<len(arr)-1):
        x = arr[i]
        y = arr[i+1]
        if opposite(x,y):
            del arr[i]
            del arr[i]
            i = 0
        else: i+=1
    return arr

TEST_CODE_diana_henninger = '''
result = diana_henninger_day13(["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"])
'''

Jose_Catela_setup = '''
from __main__ import Jose_Catela_day13
'''

def Jose_Catela_day13(arr):
    cases = ['NORTHSOUTH', 'SOUTHNORTH', 'EASTWEST', 'WESTEAST']
    position = 0
    while len(arr) != 0 and position != len(arr) - 1:
        to_test = arr[position] + arr[position+1]
        if to_test in cases:
            arr.pop(position)
            arr.pop(position)
            position = 0
        else:
            position += 1
    return arr

TEST_CODE_Jose_Catela = '''
result = Jose_Catela_day13(["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"])
'''

Jens_setup = '''
from __main__ import Jens_day13
'''

def Jens_day13(arr):
    dir = ' ' + ' '.join(arr) + ' '
    for i in range(len(arr)//2):
        dir = dir.replace(' NORTH SOUTH ', ' ').replace(' SOUTH NORTH ', ' ').replace(' EAST WEST ', ' ').replace(' WEST EAST ', ' ')
    return dir.strip().split()

TEST_CODE_Jens = '''
result = Jens_day13(["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"])
'''

kilian_setup = '''
from __main__ import kilian_day13
'''

def kilian_day13(arr):
    i = 1
    while i < len(arr):
        if (arr[i] == 'NORTH') and (arr[i - 1] == 'SOUTH'):
            del arr[i-1]
            del arr[i-1]
        elif (arr[i] == 'SOUTH') and (arr[i - 1] == 'NORTH'):
            del arr[i-1]
            del arr[i-1]
        elif (arr[i] == 'WEST') and (arr[i - 1] == 'EAST'):
            del arr[i-1]
            del arr[i-1]
        elif (arr[i] == 'EAST') and (arr[i - 1] == 'WEST'):
            del arr[i-1]
            del arr[i-1]
        elif i == len(arr) - 1:
            break
        elif (arr[i] == 'NORTH') and (arr[i + 1] == 'SOUTH'):
            del arr[i]
            del arr[i]
        elif (arr[i] == 'SOUTH') and (arr[i + 1] == 'NORTH'):
            del arr[i]
            del arr[i]
        elif (arr[i] == 'WEST') and (arr[i + 1] == 'EAST'):
            del arr[i]
            del arr[i]
        elif (arr[i] == 'EAST') and (arr[i + 1] == 'WEST'):
            del arr[i]
            del arr[i]
        else:
            i += 1
    return arr

TEST_CODE_kilian = '''
result = kilian_day13(["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"])
'''

Kurt_Hinderer_setup = '''
from __main__ import Kurt_Hinderer_day13
'''

def Kurt_Hinderer_day13(directions):
    #damn, no vectors, have to fudge it
    dir_dict = {"NORTH": -1, "SOUTH": 1, "EAST": -2, "WEST": 2}
    done = False
    while not done:
        i = 0
        deleted = False
        while i < len(directions)-1 and not deleted:
            if dir_dict[directions[i]] + dir_dict[directions[i+1]] == 0:
                del directions[i: i+2]
                deleted = True
            i += 1
        done = not deleted
    return directions

TEST_CODE_Kurt_Hinderer = '''
result = Kurt_Hinderer_day13(["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"])
'''
Oleksandra_Chmel_setup = '''
from __main__ import Oleksandra_Chmel_day13
'''

def Oleksandra_Chmel_day13(arr):
    check = {'WEST':'EAST','EAST':'WEST','NORTH':'SOUTH','SOUTH':'NORTH'}
    count = len(arr)+1
    def smaller(arr):
        for ind,dir in enumerate(arr):
            if dir and check[dir]==arr[ind-1]:
                del arr[ind-1:ind+1]
        return arr
    while len(arr)!=count:
        arr = smaller(arr)
        count -= 1
    return arr

TEST_CODE_Oleksandra_Chmel = '''
result = Oleksandra_Chmel_day13(["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"])
'''

sjay_setup = '''
from __main__ import sjay_day13
'''

def sjay_day13(arr):
    index=0
    while index <= len(arr)-2:
        if (str(arr[index]).upper() == "NORTH" and str(arr[index+1]).upper()=="SOUTH") or (str(arr[index].upper()) == "SOUTH" and str(arr[index+1]).upper()=="NORTH"):
            del arr[index:index+2]
            index =0
        elif (str(arr[index]).upper() == "EAST" and str(arr[index+1]).upper()=="WEST") or (str(arr[index]).upper() == "WEST" and str(arr[index+1]).upper()=="EAST"):
            del arr[index:index+2]
            index=0
        else:
            index = index + 1
    return arr

TEST_CODE_sjay = '''
result = sjay_day13(["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"])
'''

print("Time for akash_agarwal test code: " + str(timeit.timeit(stmt=TEST_CODE_akash_agarwal, setup=akash_agarwal_setup, number=100000)) + " seconds")
print("Time for akash_karan test code: " + str(timeit.timeit(stmt=TEST_CODE_akash_karan, setup=akash_karan_setup, number=100000)) + " seconds")
print("Time for ccquiel test code: " + str(timeit.timeit(stmt=TEST_CODE_ccquiel, setup=ccquiel_setup, number=100000)) + " seconds")
print("Time for Charlie_Ang test code: " + str(timeit.timeit(stmt=TEST_CODE_Charlie_Ang, setup=Charlie_Ang_setup, number=100000)) + " seconds")
print("Time for diana_henninger test code: " + str(timeit.timeit(stmt=TEST_CODE_diana_henninger, setup=diana_henninger_setup, number=100000)) + " seconds")
print("Time for Jens test code: " + str(timeit.timeit(stmt=TEST_CODE_Jens, setup=Jens_setup, number=100000)) + " seconds")
print("Time for Jose_Catela test code: " + str(timeit.timeit(stmt=TEST_CODE_Jose_Catela, setup=Jose_Catela_setup, number=100000)) + " seconds")
print("Time for kilian test code: " + str(timeit.timeit(stmt=TEST_CODE_kilian, setup=kilian_setup, number=100000)) + " seconds")
print("Time for Kurt_Hinderer test code: " + str(timeit.timeit(stmt=TEST_CODE_Kurt_Hinderer, setup=Kurt_Hinderer_setup, number=100000)) + " seconds")
print("Time for Oleksandra_Chmel test code: " + str(timeit.timeit(stmt=TEST_CODE_Oleksandra_Chmel, setup=Oleksandra_Chmel_setup, number=100000)) + " seconds")
print("Time for sjay test code: " + str(timeit.timeit(stmt=TEST_CODE_sjay, setup=sjay_setup, number=100000)) + " seconds")
