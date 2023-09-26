x = [int(x) for x in input("?").split(" ")]
s = 0
if x[0] % 2 == 0 and x[1] % 2 == 0:
    s = 2
elif x[0] % 3 == 0 and x[1] % 3 == 0:
    s = 3
elif x[0] % 5 == 0 and x[1] % 5 == 0:
    s = 5
elif x[0] % 7 == 0 and x[1] % 7 == 0:
    s = 7
res = (x[0]*x[1])//s
print(res)