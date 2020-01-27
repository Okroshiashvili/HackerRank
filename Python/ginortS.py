
# Very naive solution

myList = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1357902468"

print(*sorted(input(), key = myList.index), sep ="")



