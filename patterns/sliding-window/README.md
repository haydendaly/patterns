---
description: >-
  https://github.com/haydendaly/experiments/blob/main/patterns/sliding_windows.ipynb
---

# Sliding Window

## What is the sliding window pattern?

The sliding window pattern is used to perform a specific query on a sub-array of a given array or linked list, such as finding the longest subarray containing all 1s. Sliding Windows start from the 1st element and keep shifting right by one element and adjust the length of the window according to the problem that you are solving. In some cases, the window size remains constant and in other cases the sizes grows or shrinks.

### Requirements

* Input is a linear data structure (linked list, array, or string)
* Asked to find the longest/shortest substring, subarray, or a desired value

## Example Problem: Minimum Size Subarray Sum

_Original Problem:_ [_LeetCode #209_](https://leetcode.com/problems/minimum-size-subarray-sum/)__

Given an array of positive numbers and a positive number `target`, find the length of the smallest contiguous subarray whose sum is greater than or equal to `target`. Return `0` if no such subarray exists.

### Starter Code

```python
def smallest_subarray_with_target_sum(target, nums):
    """Takes array of integers nums and integer target, returns smallest subarray with sum equivalent to target"""
    pass
    
# Test Case 1
target, nums, ans = 7, [2, 1, 5, 2, 3, 2], 2
assert smallest_subarray_with_target_sum(target, nums) == ans
```

### Solution

```python
def smallest_subarray_with_target_sum(target, nums):
    running_sum, start = 0, 0
    smallest = float('inf')
    for end, num in enumerate(nums):
        running_sum += num
        while running_sum >= s:
            smallest = min(smallest, end - start + 1)
            running_sum -= nums[start]
            start += 1
    return smallest if smallest != float('inf') else -1
```

\


