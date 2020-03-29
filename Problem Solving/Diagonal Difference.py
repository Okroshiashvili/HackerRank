


n = int(input())

a = []

for _ in range(n):
    a.append(list(map(int, input().rstrip().split())))



def diagonalDifference(a):
        main_diag = sum(a[i][i] for i in range(n))
        non_main_diag = sum(a[i][n-i-1] for i in range(n))
        x = abs(main_diag - non_main_diag)
        return x

diagonalDifference(a)

###

# Second Solution using Numpy

n = int(input())

a = []

for _ in range(n):
    a.append(list(map(int, input().rstrip().split())))
    
    
def diagonalDifference(a):
    import numpy as np
    main_diag_sum = np.trace(a)
    b = np.asarray(a)
    b = np.fliplr(b)
    non_main_diag_sum = np.trace(b)
    return abs(main_diag_sum - non_main_diag_sum)

diagonalDifference(a)



