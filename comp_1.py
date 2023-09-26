def maximumSumQueries(nums1, nums2, queries):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :type queries: List[List[int]]
    :rtype: List[int]

    """
    res = []
    q_1 = []
    q_2 = []
    prob_1 = []
    prob_2 = []
    def busq_binaria(nums,index,indexes):
        if num
    for i in range(len(queries)):
        maxi = 0
        que = queries[i]
        q_1 = [nums1.index(x) for x in nums1 if x >= que[0]]
        q_2 = [nums2.index(x) for x in nums2 if x >= que[1]]
        prob_1 = list(set(q_1))
        prob_2 = list(set(q_2))
        if prob_1 != q_1:
        print("w",q_1,q_2,que)
        for j in range(len(q_1)):
            for t in range(len(q_2)):
                cont = 0
                print("q",nums1[q_1[j]], nums1[q_2[t]], q_1[j],q_2[t])
                if q_1[j] == q_2[t]:
                    print("t",nums1[q_1[j]],nums2[q_2[t]])
                    cont = nums1[q_1[j]] + nums2[q_2[t]]
                if cont > maxi:
                    maxi = cont
                print("m",maxi)
        if maxi == 0:
            res.append(-1)
        else:
            res.append(maxi)
    if len(res) == 0:
        return [-1]
    else:
        return res
def main():
    x = list(map(int,input("?").split(",")))
    y = list(map(int,input("?").split(",")))
    z = int(input("?"))
    q = []
    t = []
    for i in range(z):
        t = list(map(int,input("?").split(",")))
        q.append(t)
    print(maximumSumQueries(x,y,q))
main()
