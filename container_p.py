def max(height):
    i = 0
    j = len(height)-1
    l = 0
    r = 0
    ma = 0
    if len(height) == 2:
        return 2 * min(height[0],height[1])
    while i != j:
        t = ((j - i) * min(height[i], height[j]))
        print(ma, l, r)
        print(i,j,t)
        print(height[i],height[j])
        print(j-i)
        if ma < t:
            ma = t
        if height[i] < height[j]:
            i += 1
            r = height[j]
        elif height[i] > height[j]:
            j -= 1
            l = height[i]
        else:
            i += 1
            r = height[j]


    return ma
def main():
    r = list(map(int,input().split(",")))
    print(max(r))
main()