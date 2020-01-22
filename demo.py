from itertools import cycle

def fun(n, endnode):
    nums = []
    for i in range(n):
        nums.append(i)
    #pool = cycle(nums)
    dic = {}
    for i in range(len(endnode)-1):
        
        a = endnode[i]
        b = endnode[i+1]
        if a<=b:
            for j in range(a, b+1):
                dic[j] = dic.get(j, 0) +1
        else:
            for j in nums[a:b-1]:
                dic[j] = dic.get(j, 0) +1
    
    maxVis = -1
    maxVal = -1
    for k, v in dic.items():
        if v == maxVis:
            if maxVal< k:
                maxVal = k
        elif v>maxVis:
            maxVis = v
            maxVal = k
    return k

print(fun(4,[1,5,10,5]))
            


    