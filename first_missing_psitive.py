def problem(nums):
        if len(nums) == 1:
            if 1 > nums[0] <= 0:
                return 1
            else:
                return 2
        nums = list(map(int, sorted(nums)))
        j = [x for x in nums if x > 0]
        if not j:
            return 1
        if len(j) == 2:
            if j[0] == j[1] == 1:
                return 2
            if j[0] == j[1] != 1 or j[0] != 1:
                return 1
            if 1 == j[0] == j[1] - 1:
                return 3
        i,t = 1,1
        while i < len(j) and (j[i] == j[i - 1] + 1 or j[i] == j[i - 1]):
            if j[i] == j[i - 1]:
                i += 1
            if i < len(j):
                if j[i] == j[i - 1] + 1:
                    i += 1
                    t += 1
            print(i)
        if j[0] != 1:
            return 1
        if j[0] == 1:
            return j[0] + t
def main():
    print(problem((list(sorted(map(int,input("?").split(",")))))))
main()