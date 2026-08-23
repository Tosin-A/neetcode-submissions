class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        temp = ""
        for i in range (len(nums)):
            for j in range (len(nums) - 1):
                if  nums[i] + nums[j]  == target and i != j:
                    if j < i:
                        temp = i
                        i = j
                        j = temp
                    return [i, j]            