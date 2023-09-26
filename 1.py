s = input("?")
r = []
num = []
for i in range(len(s)):
    if s[i] not in r:
        r.append(s[i])
        num.append(s.count(s[i]))
mas = max(num)
q = num.index(mas)
sa = r[q]
print(sa,"-->",mas)
