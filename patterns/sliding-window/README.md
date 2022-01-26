---
description: >-
  https://github.com/haydendaly/experiments/blob/main/patterns/sliding_windows.ipynb
---

# Sliding Window

## What is the sliding window pattern?

The sliding window pattern is used to perform a query on a sub-array of a given array or linked list, such as finding the longest subarray containing all `1`'s. Sliding windows start from the `0`th element and keep shifting right, adjusting the length of the window according to the problem that you are solving. In some cases, the window size remains constant and in other cases the size grows or shrinks.

### Requirements

* Input is a linear data structure (linked list, array, or string)
* Asked to find the longest/shortest substring, subarray, or a desired value

## Max Consecutive Ones III

_Original Problem:_ [_LeetCode #1004 (Medium)_](https://leetcode.com/problems/max-consecutive-ones-iii/)

Given a binary array `nums` and an integer `k`, return the maximum number of consecutive `1`'s in the array if you can flip at most `k` `0`'s.

### Starter Code

```python
def longest_ones(nums, k):
    """Given array of integers nums and integer k, return the longest contiguous subarray of ones if you are able to change k values"""
    pass

# Test Case 1
nums, k, ans = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], 2, 6
assert longest_ones(nums, k) == ans

# Test Case 2
nums, k, ans = [0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1], 3, 10
assert longest_ones(nums, k) == ans
```

### Solution

```python
def longest_ones(nums, k):
    start, max_len, diff = 0, 0, 0
    for end, num in enumerate(nums):
        if num == 0:
            diff += 1
        while diff > k:
            if nums[start] == 0:
                diff -= 1
            start += 1
        max_len = max(max_len, end - start + 1)
    return max_len
```

## Minimum Size Subarray Sum

_Original Problem:_ [_LeetCode #209 (Medium)_](https://leetcode.com/problems/minimum-size-subarray-sum/)__

Given an array of positive numbers and a positive number `target`, find the length of the smallest contiguous subarray whose sum is greater than or equal to `target`. Return `0` if no such sub-array exists.

### Starter Code

```python
def smallest_subarray_with_target_sum(target, nums):
    """Takes array of integers nums and integer target, returns smallest sub-array with sum equivalent to target"""
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


