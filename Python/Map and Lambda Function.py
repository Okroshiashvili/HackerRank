

cube = lambda x: x**3 # complete the lambda function 

def fibonacci(n):
    # return a list of fibonacci numbers
    out = [0, 1]

    [out.append(out[i-2]+out[i-1]) for i in range(2,n)]

    return out[0:n]

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))


