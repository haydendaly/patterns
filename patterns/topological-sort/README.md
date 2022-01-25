# Topological Sort

## What is a topological sort?

Topological Sort is an algorithm used to find a linear ordering of elements that have dependencies on each other. For example, if even `B` is dependent on event `A`, `A` comes before `B` in topological ordering.

### Algorithm

Topological Sort of a directed graph (a graph with unidirectional edges) is a linear ordering of its vertices such that for every directed edge (U, V) from vertex U to vertex V, U comes before V in the ordering.

Given a directed graph, find the topological ordering of its vertices.

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
```

Simplest example is [LeetCode #207](https://leetcode.com/problems/course-schedule/)
