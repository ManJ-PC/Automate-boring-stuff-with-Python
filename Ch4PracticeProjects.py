#  ******************  Pratice Project  ******************  # 


################### 1 ####################

print("\n\n#### 1st Practice Problem: Oxford Comma ####\n")
def str_converter(list):
    size = len(list)
    str = ""
    while size > 0:
        if size == 1:
            str += list[-size]
        if size == 2:
            str += list[-size] + " and "
        elif size > 2:
            str += list[-size] + ", "
        size -= 1
    return str

fruits = ['apples', 'bananas', 'tofu', 'cats']
print("My Solution:", str_converter(fruits))


 # Solution

"""Comma Code."""

spam = ['apples', 'bananas', 'tofu', 'cats']


def list_joiner(list):
    """Take a list and print it as an Oxford comma having sentence."""
    count = 0
    joined = ''
    while count < len(list) - 2:
        joined += list[count] + ', '
        count += 1
    joined += list[-2] + ' and '
    joined += list[-1] + '.'
    return joined


print("Solution:", list_joiner(spam))

print("****************************************************")


################### 2 ####################
print("\n\n\n#### 2st Practice Problem: Coin Flip, number of 6 Streak ,.. probability ####\n\n")

# The possibility of a streak of 6 heads or tails in a row with 100 coin flips is 1.56%., I consider 3,125% because the first flip is already guaranteed, so We should be 
print("Segundo os cálculos para o problema pensado por mim:", pow(0.5,5)) # o primeiro já é garantido

import random
numberOfStreaks = 0
seq = 1
lastval = 2
verify_streak = 0
numberOfStreaks = 0
for experimentNumber in range(10000):
  streak = 0
  for i in range(100): # Code that creates a list of 100 'heads' or 'tails' values.
    val = random.randint(0, 1)
    if val == 0:
        pass #print('H',sep='') #, end='')
    else:
        pass#print('T',sep='')
    if val == lastval:
        seq += 1
        # Code that checks if there is a streak of 6 heads or tails in a row.
        if seq >= 6:
          streak += 1
    else:
       seq = 1
    #print(seq)
    lastval = val
    #print("Streak:", streak)
  if streak > 0:
     verify_streak += 1  
  #print("Number of Streaks: ", streak)
  #print("Chance of streak: %s%%" % (streak / 100))
  numberOfStreaks += streak
print('\n\nTotal of chances streak: %s%%' % (numberOfStreaks *100/ (10000*100)))

print('\nProbability of streak: %s%%' % (verify_streak *100/ 10000))


################### 3 ####################

grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

width = len(grid[0]) # 6
heigth = len(grid) # 9

def grid_printer(grid):
    for x in range(width):
        linha = []
        for y in range(heigth):
            linha.append(grid[y][x])
        print(linha)

grid_printer(grid)

# Solution


for i in range(len(grid[0])):
    for j in range(len(grid)):
        print(grid[j][i], end='')
    print()


