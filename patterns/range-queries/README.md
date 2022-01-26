# Range Queries

## What are range queries?

Range queries are queries applied across ranges on data structures. Common examples of range queries are:

* `sum(i, j)`: the sum of values in range `[i, j]`.
* `min(i, j)`: the minimum value in range `[i, j]`.
* `max(i, j)`: the maximum value in range `[i, j]`.

To compute these operations on a standard array naively takes linear `O(n)` time. If you are doing these queries across multiple sub-ranges, you can end up writing an `O(n^2)` algorithm.

In this chapter, we are going to focus on data structures that allow us to complete these queries in constant `O(1)` time.

### Data Structures

Explain prefix sums here with diagrams.

## Range Sum Query

_Original Problem:_ [_LeetCode #303 (Easy)_](https://leetcode.com/problems/range-sum-query-immutable/)

Given an integer array `nums`, handle multiple queries of the following type:

1. Calculate the **sum** of the elements of `nums` between indices `i` and `j` **inclusive** where `i <= j`.

Implement the `NumArray` class:

* `NumArray(nums)` Initializes the object with the integer array `nums`.
* `sum_range(i, j)` Returns the **sum** of the elements of `nums` between indices `i` and `j` **inclusive.**

### Solution

```python
class NumArray:
    def __init__(self, nums):
        self.prefix_sum = [0] * (len(nums) + 1)
        for i, num in enumerate(nums):
            self.prefix_sum[i + 1] = self.prefix_sum[i] + num
            
    def sum_range(self, i, j):
        return self.prefix_sum[j + 1] - self.prefix_sum[i]
```
