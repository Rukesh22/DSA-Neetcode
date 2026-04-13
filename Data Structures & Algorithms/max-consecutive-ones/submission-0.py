class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:

        n = len(nums)

        count = 0
        maxi = 0

        for i in range(0,n):
            if nums[i] == 1:
                count += 1

            else:
                count = 0

            maxi = max(maxi, count)
        return maxi

- Time Complexity: O(N), since we scan the array once.
- Space Complexity: O(1), as only constant extra variables are used.
