

from collections import deque


for _ in range(int(input())):
    input()

    sideLength = deque(map(int, input().strip().split()))
    answer = "Yes"

    if max(sideLength) not in (sideLength[0], sideLength[-1]):
        answer = "No"
    print(answer)





