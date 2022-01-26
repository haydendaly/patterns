---
description: >-
  https://github.com/haydendaly/experiments/blob/main/patterns/disjoint_sets.ipynb
---

# Disjoint Sets / Union Find

## What is a disjoint set?

A clever data structure.

William Fiset explains it really well on YouTube.

{% embed url="https://www.youtube.com/watch?v=ibjEGG7ylHk" %}
William Fiset: Union Find Introduction
{% endembed %}

### When to use?

If you have a set of N elements partitioned into further subsets, and you have to keep track of the connectivity of each element in a particular subset or connectivity of subsets with each other. You can manage connectivity/mappings easily with disjoint sets and the union find operation.

## Find the Duplicate Number

_Original Problem:_ [_LeetCode #287 (Medium)_](https://leetcode.com/problems/find-the-duplicate-number/)

Given an array of integers `nums` containing `n + 1` integers where each integer is in the range `[1, n]` inclusive.

There is only one repeated number in `nums`, return this repeated number. Your solution must use constant extra space.

### Starter Code

```python
def find_duplicate(nums):
    """Takes in an array nums, returns duplicate number"""
    pass

# Test Case 1
nums, ans = [1, 3, 4, 2, 2], 2
assert find_duplicate(nums) == ans

# Test Case 2
nums, ans = [3, 1, 3, 4, 2], 3
assert find_duplicate(nums) == ans
```

### Solution

```python
def find_duplicate(nums): 
    for num in nums: 
        if nums[abs(num) - 1] < 0: 
            return abs(num) 
        nums[abs(num) - 1] *= -1 
    return -1
```

The solution is linear runtime `O(n)` and constant space `O(1)`. This solution works by using an inputted data structure as a disjoint set. Each value of `nums` maps to its index by the function `def idx(num): num - 1` . An example mapping is the value `9` to the index `8`. This direct mapping takes advantage of the input constraints of values being in the range `[1, n]` and the array being modifiable.

Mapping allows you to store information for each number at the index returned by this function. If we multiply the value at this mapped index by `-1`, we can keep a boolean record on whether or not a certain number has been seen. Once we have a record of what has been seen by all previous elements, we can easily know when we reach a duplicate in iteration.

Since some numbers are now negative, we have to have to do `abs(num)` so we don't accidentally check a negative index. This can be used to detect if this value has already been "visited" and is a flattened way of performing an algorithm like union find.
