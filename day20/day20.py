import timeit
import re


akash_karan_setup = '''
from __main__ import akash_karan_day20
'''

def akash_karan_day20(string):
    fl=0
    s=[]
    for i in string:
        if(i==")" and fl==0 ):
            return False
        elif(i=="("):
            s.append("(")
            fl=1
        elif(i==")"):
            try:
                s.pop()
            except(IndexError):
                return False
            fl=1
    return not len(s)

TEST_CODE_akash_karan = '''
result = akash_karan_day20("(())((()())())")
'''

ccquiel_setup = '''
from __main__ import ccquiel_day20
'''

def ccquiel_day20(string):
    valsum =0    
    for s in string:
        if s == '(':
            valsum += 1
        elif s == ')':
            valsum -= 1
        if valsum < 0:
            return False
    if valsum == 0:
        return True
    else:
        return False

TEST_CODE_ccquiel = '''
result = ccquiel_day20("(())((()())())")
'''

charlie_ang_setup = '''
from __main__ import charlie_ang_day20
'''

def charlie_ang_day20(string):
    #print("Working with {}".format(string))
    pattern = re.compile(r'\(\w*\)')
    working = string
    while pattern.search(working):
        working = pattern.sub("", working)
    return not re.search(r'\(|\)', working)

TEST_CODE_charlie_ang = '''
result = charlie_ang_day20("(())((()())())")
'''

diana_henninger_setup = '''
from __main__ import diana_henninger_day20
'''

def diana_henninger_day20(string):
    stack = []
    for c in string:
        if c == '(': stack.append(c)
        elif c == ')': 
            if len(stack)==0: return False
            else: stack.pop()
    return len(stack)==0

TEST_CODE_diana_henninger = '''
result = diana_henninger_day20("(())((()())())")
'''

Jens_setup = '''
from __main__ import Jens_day20
'''

def Jens_day20(string):
    open_parentheses = 0
    for letter in string:
        if letter == '(':
            open_parentheses += 1
        elif letter == ')':
            open_parentheses -= 1
        if open_parentheses < 0:
            return False
    return True if open_parentheses == 0 else False

TEST_CODE_Jens = '''
result = Jens_day20("(())((()())())")
'''

Jose_Catela_setup = '''
from __main__ import Jose_Catela_day20
'''

def Jose_Catela_day20(string):
    string2 = ''
    for character in string:
        if character == '(' or character == ')':
            string2 += character
    stack = []
    for character in string2:
        if character == '(':
            stack.append(character)
        else:
            if len(stack) == 0:
                return False
            stack.pop()
    return len(stack) == 0

TEST_CODE_Jose_Catela = '''
result = Jose_Catela_day20("(())((()())())")
'''

kilian_setup = '''
from __main__ import kilian_day20
'''

def kilian_day20(string):
    count = 0
    for paranthese in string:
        if paranthese == '(':
           count += 1
        elif paranthese == ')':
            count -= 1
        if count < 0: return False
    return count == 0

TEST_CODE_kilian = '''
result = kilian_day20("(())((()())())")
'''

Krzysztof_Blach_setup = '''
from __main__ import Krzysztof_Blach_day20
'''

def Krzysztof_Blach_day20(string):
    if len(string) == 0:
        return True
    paren_str = ''
    for char in string:
        if char == '(' or char == ')':
            paren_str += char
    for i in range(len(paren_str) - 1):
        if paren_str[i] == '(' and paren_str[i + 1] == ')':
            return Krzysztof_Blach_day20(paren_str[:i] + paren_str[i + 2:])
    return False

TEST_CODE_Krzysztof_Blach = '''
result = Krzysztof_Blach_day20("(())((()())())")
'''

Kurt_Hinderer_setup = '''
from __main__ import Kurt_Hinderer_day20
'''

def Kurt_Hinderer_day20(string):
    paren_level = 0
    for i in range(len(string)):
        if string[i] == '(':
            paren_level += 1
        elif string[i] == ')':
            if paren_level < 1:
                paren_level = -1000
            else:
                paren_level -= 1
    return paren_level == 0

TEST_CODE_Kurt_Hinderer = '''
result = Kurt_Hinderer_day20("(())((()())())")
'''

Oleksandra_Chmel_setup = '''
from __main__ import Oleksandra_Chmel_day20
'''

def Oleksandra_Chmel_day20(string):
    ans = ''
    for i in string:
        if i in ('(',')'):
            ans += i
    while '()' in ans:
        ans = ans.replace('()','')
    return ans == ''

TEST_CODE_Oleksandra_Chmel = '''
result = Oleksandra_Chmel_day20("(())((()())())")
'''

Samrat_Mukherjee_setup = '''
from __main__ import Samrat_Mukherjee_day20
'''

def Samrat_Mukherjee_day20(string):
    #your code here
    stack  = []
    for char in string:
        if char == '(':
            stack.append(char)
        else:
            try:
                if char == ')':
                    del stack[-1]
            except:
                return False
    if len(stack) == 0:
        return True
    else:
        return False

TEST_CODE_Samrat_Mukherjee = '''
result = Samrat_Mukherjee_day20("(())((()())())")
'''

sjay_setup = '''
from __main__ import sjay_day20
'''

def sjay_day20(string):
    flag = False
    openpara = list(numb for numb,item in enumerate(string) if item=="(")
    closepara = list(numb for numb,item in enumerate(string) if item==")")
    data = zip(openpara,closepara)
    #print(openpara,closepara)
    for item in data:
        #print(item)
        if isinstance(item[0],int)and isinstance(item[1],int):
            if item[0] < item[1]:
                flag = True
            else:
                flag = False
                break
        else:
            flag=False
            break
    if len(openpara)==0 and len(closepara)==0:
        flag=True
    elif len(openpara)!= len(closepara):
        flag=False
    return flag

TEST_CODE_sjay = '''
result = sjay_day20("(())((()())())")
'''

Vanessa_G_setup = '''
from __main__ import Vanessa_G_day20
'''

def Vanessa_G_day20(string):
    count_left = 0
    count_right = 0
    for c in string:
        if count_left < count_right: return False
        elif c == '(': count_left += 1
        elif c == ')': count_right += 1
    return count_left == count_right

TEST_CODE_Vanessa_G = '''
result = Vanessa_G_day20("(())((()())())")
'''

print("Time for akash_karan test code: " + str(timeit.timeit(stmt=TEST_CODE_akash_karan, setup=akash_karan_setup, number=100000)) + " seconds")
print("Time for ccquiel test code: " + str(timeit.timeit(stmt=TEST_CODE_ccquiel, setup=ccquiel_setup, number=100000)) + " seconds")
print("Time for charlie_ang test code: " + str(timeit.timeit(stmt=TEST_CODE_charlie_ang, setup=charlie_ang_setup, number=100000)) + " seconds")
print("Time for diana_henninger test code: " + str(timeit.timeit(stmt=TEST_CODE_diana_henninger, setup=diana_henninger_setup, number=100000)) + " seconds")
print("Time for Jens test code: " + str(timeit.timeit(stmt=TEST_CODE_Jens, setup=Jens_setup, number=100000)) + " seconds")
print("Time for Jose_Catela test code: " + str(timeit.timeit(stmt=TEST_CODE_Jose_Catela, setup=Jose_Catela_setup, number=100000)) + " seconds")
print("Time for kilian test code: " + str(timeit.timeit(stmt=TEST_CODE_kilian, setup=kilian_setup, number=100000)) + " seconds")
print("Time for Krzysztof_Blach test code: " + str(timeit.timeit(stmt=TEST_CODE_Krzysztof_Blach, setup=Krzysztof_Blach_setup, number=100000)) + " seconds")
print("Time for Kurt_Hinderer test code: " + str(timeit.timeit(stmt=TEST_CODE_Kurt_Hinderer, setup=Kurt_Hinderer_setup, number=100000)) + " seconds")
print("Time for Oleksandra_Chmel test code: " + str(timeit.timeit(stmt=TEST_CODE_Oleksandra_Chmel, setup=Oleksandra_Chmel_setup, number=100000)) + " seconds")
print("Time for Samrat_Mukherjee test code: " + str(timeit.timeit(stmt=TEST_CODE_Samrat_Mukherjee, setup=Samrat_Mukherjee_setup, number=100000)) + " seconds")
print("Time for sjay test code: " + str(timeit.timeit(stmt=TEST_CODE_sjay, setup=sjay_setup, number=100000)) + " seconds")
print("Time for Vanessa_G test code: " + str(timeit.timeit(stmt=TEST_CODE_Vanessa_G, setup=Vanessa_G_setup, number=100000)) + " seconds")
