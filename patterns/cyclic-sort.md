---
description: https://github.com/haydendaly/experiments/blob/main/patterns/cyclic_sort.ipynb
---

# Cyclic Sort

## What is a cyclic sort?

The cyclic sort pattern describes an interesting approach to deal with problems involving arrays containing numbers in a given range.

## Missing Number

_Original Problem:_ [_LeetCode #268_](https://leetcode.com/problems/missing-number/)__

Given an array `nums` containing `n` distinct numbers in the range `[0, n]`, return the only number in the range that is missing from the array.

### Starter Code

```python
def find_missing_number(nums):
    """Takes array of integers nums in range [0, n], returns missing number"""
    pass
    
# Test Case 1
nums, ans = [8, 3, 5, 2, 4, 6, 0, 1], 7
assert find_missing_numbers(nums) == ans
```

### Solution

```python
def find_missing_number(nums):
    i = 0
    while i < len(nums):
        target = nums[i]
        if nums[i] < len(nums) and nums[i] != nums[target]:
            nums[i], nums[target] = nums[target], nums[i]
        else:
            i += 1
    for i, num in enumerate(nums):
        if i != num:
            return i
    return -1 if len(nums) in nums else len(nums)
```
