class Solution:
    def nthUglyNumber(self, n: int) -> int:
        res=[1]
        tw=th=fv=0
        for i in range(1,n):
            k=min(res[tw]*2,res[th]*3,res[fv]*5)
            res.append(k)
            if (res[tw]*2)==k:tw+=1
            if (res[th]*3)==k:th+=1
            if (res[fv]*5)==k:fv+=1
        return res[-1]
    