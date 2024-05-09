def containsNearbyDuplicate(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: bool
    """
    #check if length of nums is equal to length of set of nums if yes return False
    #else iterate through the list and check if the element at index i is equal to element at index j and the difference between i and j is 
    #less than or equal to k then return True 
    if len(nums) == len(set(nums)):
        return False
    else:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j] and abs(i-j) <= k:
                    return True
        return False