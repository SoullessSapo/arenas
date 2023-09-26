def comp(s):
    cont = [s.index(x) for x in s if s.count(x) == 2]
    if len(cont) == 0 and s[0] == s[1::len(s)-1]:
        return s[0] + s[1]
    t = [s.index(x) for x in s if s.count(x) > 1]
    if len(cont) == 0 and len(t) == 0:
        return len(s)
    if len(cont) == 0 and len(t) != 0:
        f = t[0]
        q = 0
        for i in range(1,len(t)):
            q = t[i] - t[i-1]
            if q > f:
                f = q
        return q
    c = []
    for i in range(len(cont)):
        i = cont[i]
        j = cont[i] + 1
        co = 0
        maxi = 0
        if i != 0 and j != len(s)-1 and s[i] == s[j]:
            while s[i] != s[i-1] and s[j] != s[j+1] and j != len(s)-1 and i != 0:
                i += 1
                j -= 1
                co = i - j
                if co > maxi:
                      maxi = co
        c.append(maxi)
    return max(c)
def main():
    print(comp(input("?")))
main()
