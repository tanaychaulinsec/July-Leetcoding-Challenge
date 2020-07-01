#using sreedhar acharya formula
class Solution:
    def arrangeCoins(self, n: int) -> int:
        d=sqrt(1+8*n)
        ans=(1+d)//2
        return int(ans-1)

#Binary search O(logn)
class Solution:
    def arrangeCoins(self, n: int) -> int:
        low=0
        high=n
        while low<=high:
            mid=(low+high)//2
            m=mid*(mid+1)//2
            if m==n:
                return mid
            elif m<n:
                low=mid+1
            else:
                high=mid-1
        return high