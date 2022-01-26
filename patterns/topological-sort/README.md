---
description: >-
  https://github.com/haydendaly/experiments/blob/main/patterns/topological_sort.ipynb
---

# Topological Sort

## What is a topological sort?

Topological Sort is an algorithm used to find a linear ordering of elements that have dependencies on each other. For example, if event `B` requires completion of event `A`, `A` comes before `B` in topological ordering.

![Dependency graph to linear ordering](../../.gitbook/assets/top\_sort.png)

This only works when we are provided with a directed-acyclic graph (DAG) which is jargon for a graph with no cycles. We can't have cycles or an ordering is impossible. In software engineering, this often referred to as the anti-pattern of circular dependencies. There are multiple valid orderings to most directed-acyclic graphs.

### Algorithm

The general algorithm involves a few steps:

1. Convert inputted graph to adjacency list
2. Iterate over queue
3. ...

The algorithm below looks daunting but read through the comments and it'll make sense.

```python
from collections import deque

def topological_sort(vertices, edges):
    result = []
    if vertices <= 0:
        return result

    in_degree = { i: 0 for i in range(vertices) }
    graph = { i: [] for i in range(vertices) }

    for edge in edges:
        parent, child = edge[0], edge[1]
        graph[parent].append(child)
        in_degree[child] += 1

    sources = deque()
    for key in in_degree:
        if in_degree[key] == 0:
          sources.append(key)

    while sources:
        vertex = sources.popleft()
        result.append(vertex)
        for child in graph[vertex]:
            in_degree[child] -= 1
            if in_degree[child] == 0:
                sources.append(child)

    if len(result) != vertices:
        return []

    return result
    
# Test Case 1
vertices, edges = 7, [[6, 4], [6, 2], [5, 3], [5, 4], [3, 0], [3, 1], [3, 2], [4, 1]]
possible_ans = [5, 6, 3, 4, 0, 2, 1]
```

## Course Schedule

_Original Problem:_ [_LeetCode #207_](https://leetcode.com/problems/course-schedule/)__

There are a total of `num_courses` courses you have to take, labeled from `0` to `num_courses - 1`. You are given an array `prerequisites` where `prerequisites[i] = [a, b]` indicates that you **must** take course `b` first if you want to take course `a`.

* For example, the pair `[0, 1]`, indicates that to take course `0` you have to first take course `1`.

Return `true` if you can finish all courses. Otherwise, return `false`.

### Starter Code

```python
def find_course_order(num_courses, prerequisites):
    """Takes course prerequisites, returns if possible to complete courses"""
```

### Solution

```python
def find_course_order(num_courses, prerequisites):
    in_degree = [0] * num_courses
    adj_list = [[] for _ in range(num_courses)]
    
    for curr, pre in prerequisites:
        adj_list[pre].append(curr)
        in_degree[curr] += 1
        
    q = deque()
    
    for idx, degree in enumerate(in_degree):
        if degree == 0:
            q.append(idx)
    
    result = []
    while q:
        node = q.popleft()
        result.append(node)
        if len(result) > num_courses:
            return []
        for adj_node in adj_list[node]:
            in_degree[adj_node] -= 1
            if in_degree[adj_node] == 0:
                q.append(adj_node)
        
    return result if len(result) == num_courses else []
```
