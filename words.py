def num_letters(num_rows, num_columns):
    return (num_rows*num_columns) - ((num_rows-2)*(num_columns-2))

assert num_letters(3,4)==10
assert num_letters(13,4)==30
assert num_letters(4,4)==12
assert num_letters(6,4)==16
assert num_letters(6,7)==22

import numpy as np
data = np.loadtxt("loop3.csv", delimiter=",", dtype=str, encoding='utf8')
n_rows, n_col = data.shape
words = []
#Top
c = 0
while c < n_col:
    cell = data[0, c]
    if cell != "":
        words.append(str(cell))
    c = c + 1
#Right
r = 1
while r < n_rows - 1:
    cell = data[r, n_col - 1]
    if cell != "":
        words.append(str(cell))
    r = r + 1
#Bottom
c = 0
while c < n_col:
    cell = data[n_rows - 1, c]
    if cell != "":
        words.append(str(cell))
    c = c + 1
#Left
r = 1
while r < n_rows - 1:
    cell = data[r, 0]
    if cell != "":
        words.append(str(cell))
    r = r + 1


print (words)

#Part 4
two_letters = []          
i = 0
while i < len(words):
    first = words[i]                   
    second = words[(i + 1) % len(words)]  
    word = first + second              
    two_letters.append(word)      
    i += 1                             

print("Two-letters:", two_letters)

