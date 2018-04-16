"""
Created on Mon Apr 16 14:12:09 2018

@author: Nodar.Okroshiashvili
"""


arr = []
for arr_i in range(6):
   arr_t = [int(arr_temp) for arr_temp in input().strip().split(' ')]
   arr.append(arr_t)



sum_of_hourglass = [sum(arr[i][j:j+3]) + arr[i+1][j+1] + sum(arr[i+2][j:j+3]) for i in range(0,4) for j in range(0,4)]

print(max(sum_of_hourglass))


#%%

# Second Solution


def hourglass(arr):
    res = []
    for x in range(0, 4):
        for y in range(0, 4):
            s = sum(arr[x][y:y+3]) + arr[x+1][y+1] + sum(arr[x+2][y:y+3])
            res.append(s)
    return res

result = hourglass(arr)
print(max(result))


    