class Solution:
    def twoSum(self, nums, target):
        a_dict = {}
        for i, n in enumerate(nums):
            m = target - n
            if m in a_dict:
                return [a_dict[m], i]
            a_dict[n] = i
                
        
result = Solution().twoSum([3, 6], 9)
print(result)
