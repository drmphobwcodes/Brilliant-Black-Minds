'''
Given the array nums consisting of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn].

Return the array in the form [x1,y1,x2,y2,...,xn,yn].
'''
def shuffleArray(nums, n):
    #initialize an empty list to store the shuffled array
    max_current = max_global = nums[0]
    #iterate through the list of numbers starting from the second element
    for num in nums[1:]:
        #find the maximum of the current number and the sum of the current number and the previous number
        max_current = max(num, max_current + num)
        #find the maximum of the current number and the maximum sum
        max_global = max(max_global, max_current)
    return max_global