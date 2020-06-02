
class Solution:
    def twoSum(self,nums,target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # Initialize dictionary
        table = {}
        # Iterate through list while keeping track of the paired index/value
        for index, value in enumerate(nums):
            # Get the inverse of each value
            inverse = target - value
            # Check if inverse is in dict (If so then we have seen it)
            if inverse not in table:
                table[value] = index
            else:
                return [table[inverse], index]

            