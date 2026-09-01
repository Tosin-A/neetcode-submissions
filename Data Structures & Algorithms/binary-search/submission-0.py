class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,h,c = (0, len(nums) - 1 , (len(nums)//2))
        while l <= h:
            c = l + ((h - l)// 2)
            if target < nums[c]:
                h = c - 1
            elif target > nums[c]:
                l = c + 1
            else:
                return c
        return -1



        