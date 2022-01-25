# Disjoint Sets / Union Find

### Wtf is a disjoint set?

A clever data structure.

William Fiset explains it really well on YouTube.

{% embed url="https://www.youtube.com/watch?v=ibjEGG7ylHk" %}
WilliamFiset: Union Find Introduction
{% endembed %}

### When to use?

If you have a set of N elements partitioned into further subsets, and you have to keep track of the connectivity of each element in a particular subset or connectivity of subsets with each other. You can manage connectivity easily with disjoint sets and the union find operation.

### Example Problem

#### Find the Duplicate Number&#x20;

_Original Problem:_ [_LeetCode #287 (medium)_](https://leetcode.com/problems/find-the-duplicate-number/)__

Given an array of integers `nums` containing `n + 1` integers where each integer is in the range `[1, n]` inclusive.

There is only one repeated number in `nums`, return this repeated number. Your solution must use constant extra space.

#### Solution

```python
def find_duplicate(nums): 
    for num in nums: 
        if nums[abs(num) - 1] < 0: 
            return abs(num) 
        nums[abs(num) - 1] *= -1 
    return -1
```

This solution is O(n) runtime, O(1) space. This solution works by storing the values in their indexes position by making the value negative. This can be used to detect if this value has already been "visited" and is a flattened way of performing union find.

However it modifies the input, if the input can't be modified, use the Floyd-Warshall algorithm for cycle detection.
