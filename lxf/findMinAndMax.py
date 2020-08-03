def FindMinAndMax(L):
    if L == []:
        return (None, None)
    else:
        mi = L[0]
        ma = L[0]
        for x in L:
            if x < mi:
                mi = x
        for x in L:
            if x > ma:
                ma = x
        return (mi,ma)
FindMinAndMax([1,2,3,4,56,7,-3])
