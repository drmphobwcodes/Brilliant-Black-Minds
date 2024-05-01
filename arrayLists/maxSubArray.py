'''
Given an integer array nums, find the subarray with the largest sum, and return its sum.'''


def maxSubArray(nums):
    #initialize the maximum sum to the first element of the array
    max_current = max_global = nums[0]
    #iterate through the list of numbers starting from the second element
    for num in nums[1:]:
        #find the maximum of the current number and the sum of the current number and the previous number
        max_current = max(num, max_current + num)
        #find the maximum of the current number and the maximum sum
        max_global = max(max_global, max_current)
        
    return max_global