---
description: >-
  https://github.com/haydendaly/experiments/blob/main/data-structures/binary_search.py
---

# Binary Search

## Why binary search?

You might know how to do a binary search but have trouble generalizing it to sub-problems and understanding its variations.&#x20;

```python
def binary_search(nums, target):
    low, high = 0, len(nums)
    while low <= high:
        mid = low + (high - low) // 2
        if nums[mid] < target:
            low = mid + 1
        else:
            high = mid
    return low
```

Binary search allows us to search a sorted array for a value in logarithmic `O(log(n))` time. It does this by breaking down the search space between two pointers (`low` and `high)` by checking whether a midpoint (`mid`) is greater than, less than, or equal to the target value.

The same algorithm is available in the Python standard library as `bisect` and makes the algorithm as simple as:

```python
from bisect import bisect_left

def binary_search(nums, target):
    return bisect_left(nums, target)
```

This is extremely helpful in making your code more readable. `bisect_right` is also in the library and is almost the exact same algorithm as our binary search above except changing flipping the conditional logic for determining the next iteration of bounds.

```python
if nums[mid] > target:
    high = mid
else:
    low = mid + 1    
```

This function allows us to get the upper bound of a certain number within an array. Both of these methods have the following arguments: `nums`, `target`, `lower_bound`, `upper_bound`, and `key`. `key` allows us to put in a function for what value to use instead of `nums[mid]` in the conditional above.

## Find Number Range in Sorted Array

Given an array of sorted integers containing duplicates, return the lower and upper indexes of all elements equivalent to a specified target. If there are no such elements, return `-1, -1`.

### Starter Code

```python
def binary_search_range(nums, target):
    """Returns the start and end position of the elements in nums equal to target"""
    pass
    
# Test Case 1
nums, target, ans = [0, 1, 1, 1, 3], 1, (1, 3)
assert binary_search_range(nums, target) == ans

# Test Case 2
nums, target, ans = [0, 0, 2, 3, 5, 8, 9, 9, 9], 9, (6, 8)
assert binary_search_range(nums, target) == ans
```

### Solution

```python
from bisect import bisect_left, bisect_right

def binary_search_range(nums, target):
    low = bisect_left(nums, target)
    if nums[low] != target:
        return -1, -1
    # by passing low as the lower bound for bisect_right, we narrow the search space for the upper bound
    high = bisect_right(nums, target, low) - 1
    return low, high

# Test Case 1
nums, target, ans = [0, 1, 1, 1, 3], 1, (1, 3)
assert binary_search_range(nums, target) == ans

# Test Case 2
nums, target, ans = [0, 0, 2, 3, 5, 8, 9, 9, 9], 9, (6, 8)
assert binary_search_range(nums, target) == ans

nums, target, ans = [0, 1, 1, 3, 3], 2, (-1, -1)
print(binary_search_range(nums, target))
assert binary_search_range(nums, target) == ans
```

Search rotated sorted array: [https://github.com/haydendaly/experiments/blob/main/data-structures/search\_rotated\_sorted\_array.py](https://github.com/haydendaly/experiments/blob/main/data-structures/search\_rotated\_sorted\_array.py)
