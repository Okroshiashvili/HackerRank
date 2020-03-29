


def solve(a0, a1, a2, b0, b1, b2):
    return  [sum(map(int, [a0 > b0, a1 > b1, a2 > b2])), sum(map(int, [b0 > a0, b1 > a1, b2 > a2]))]


###

def solve(a0, a1, a2, b0, b1, b2):
    #x = sum([A[0] > B[0], A[1]>B[1], A[2]>B[2]])
   # y = sum([A[0] > B[0], A[1]>B[1], A[2]>B[2]])
    x = sum([a0>b0, a1>b1,a2>b2])
    y = sum([a0<b0, a1<b1,a2<b2])
    z = [x,y]
    return z
#x = sum([A[0] > B[0], A[1]>B[1], A[2]>B[2]])

#y = sum([A[0] > B[0], A[1]>B[1], A[2]>B[2]])

z = [x,y]


a0 = 5
a1 = 6
a2 = 7
b0 = 2
b1 = 3
b2 = 7

solve(1, 2, 3, 4, 5, 6)


###


def solve(a0, a1, a2, b0, b1, b2):
    
    aliceScore, bobScore = 0, 0
    
    alice = [a0, a1, a2]
    bob = [b0, b1, b2]

    
    for i in range(3):
        if(alice[i] > bob[i]):
            aliceScore += 1
        elif(alice[i] == bob[i]):
            aliceScore += 0
            bobScore += 0
        else:
            bobScore += 1
    return [aliceScore, bobScore]

