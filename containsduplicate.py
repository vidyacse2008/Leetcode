class Solution:
    def containsDuplicate(self, nums):
         numbers = {}
         for num in nums:  
            if num in numbers:
                return True
            else:
                numbers[num] = 1
         return False