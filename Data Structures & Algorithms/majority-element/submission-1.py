class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        seen_nums = {}
        for num in nums:
            if num in seen_nums:
                seen_nums[num] += 1
            else:
                seen_nums[num] = 1
        
        for num in seen_nums:
            if seen_nums[num] > len(nums)/2:
                return num
