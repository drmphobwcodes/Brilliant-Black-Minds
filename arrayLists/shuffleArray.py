'''
Given the array nums consisting of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn].

Return the array in the form [x1,y1,x2,y2,...,xn,yn].
'''
def shuffleArray(nums, n):
    #initialize an empty list
    result = []
    #iterate through the range of n
    for i in range(n):
        #append the ith element of the nums list to the result list
        result.append(nums[i])
        #append the (i+n)th element of the nums list to the result list
        result.append(nums[i+n])
    return result