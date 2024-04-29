'''
Given an array of integers nums and integer target, return indices of the two numbers such that they add up to
target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.
'''
def twoSum(nums, target):
    #iterate through the list of numbers
    for i in range(len(nums)):
        #iterate through the list of numbers starting from the next element
        for j in range(i+1, len(nums)):
            #if the sum of the two numbers is equal to the target
            if nums[i] + nums[j] == target:
                #return the indices of the two numbers
                return [i, j]
    return None