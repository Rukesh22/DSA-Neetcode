class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        #Two pinter Approach
        #The problem asks us to remove all instances of a specific value in-place. Since the order of the remaining elements doesn't matter, we could have used a different two pointer approach, where the left pointer is initialized at 0 and the right pointer at len(nums) - 1.
        
        #However if we want to preserve the order we can use a Fast/Slow Two-Pointer approach:
        
        #The Fast Pointer (right): This pointer scans every element in the array from start to finish.
        
        #The Slow Pointer (left): This pointer keeps track of the "write" position. It only moves when we find an element that is not equal to val.
        
        #The Overwrite: Whenever right finds a valid element (element that is not equal to val), we copy it to the position of left and increment left.
        
        #By the end of the loop, all valid elements have been shifted to the front of the array. The final value of left represents the count of elements that are not equal to val.

        left = 0
        right = 0 
        
        n = len(nums)

        while right < n:
            if nums[right] != val:
                nums[left] = nums[right]
                left += 1
            right += 1

        return left

#- Time Complexity O(n): We iterate through the array exactly once.
#- Space Complexity: O(1): We modify the input array directly without using any additional data structures.