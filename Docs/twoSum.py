'''
Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.


The time complexity of this method is O(n), where n is the number of elements in the input list `nums`.

Here's why:

- The method iterates over the list `nums` exactly once. Each iteration involves constant time operations: computing `target - num`,
 looking up a value in a dictionary, returning a result, or inserting a key-value pair into a dictionary. Therefore, the time complexity of 
 the loop is O(n).

- Outside the loop, the method performs a constant amount of work: initializing an empty dictionary and returning a result. Therefore, 
the time complexity outside the loop is O(1).

Adding these together, the total time complexity of the method is O(n) + O(1) = O(n).

The space complexity of this method is also O(n), because in the worst case scenario, every element from `nums` will be stored in the 
dictionary `num_dict`.
'''




def twoSum(nums, target):
    num_dict = {}
    for i, num in enumerate(nums):
        if target - num in num_dict:
            return [num_dict[target - num], i]
        num_dict[num] = i
    return []