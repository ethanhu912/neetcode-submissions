class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        index = 0
        k = 0
        while index < len(nums):
            if nums[index] == val:
                nums.pop(nums.index(val))
            else:
                k += 1
                index += 1
        return k