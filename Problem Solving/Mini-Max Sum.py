


arr = list(map(int, input().rstrip().split()))


def miniMaxSum(arr):
    suma = sum(arr)
    minimum = suma - max(arr)
    maximum = suma - min(arr)
    print(minimum, maximum)
    
    
miniMaxSum(arr)
