#Find the Duplicate Number 
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        def f(x:int) -> bool:
            return sum(a <= x for a in nums) > x
        return bisect_left(range(len(nums)),True,key=f)