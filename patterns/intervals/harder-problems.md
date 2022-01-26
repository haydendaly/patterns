# Harder Problems

## Maximum CPU Load

_Original Problem:_ [_geeksforgeeks.org_](https://www.geeksforgeeks.org/maximum-cpu-load-from-the-given-list-of-jobs/)__

Given an array of jobs with different time requirements, where each job consists of start time, end time and CPU load. The task is to find the maximum CPU load at any time if all jobs are running on the same machine.

### Starter Code

```python
def find_max_cpu_load(jobs):
    """Takes list of job start/end times and loads, return maximum concurrent CPU load"""
    pass

# Test Case 1
jobs, ans = [(1, 4, 3), (2, 5, 4), (7, 9, 6)], 7
assert find_max_cpu_load(jobs) == ans

# Test Case 2
jobs, ans = [(6, 7, 10), (2, 4, 11), (8, 12, 15)], 15
assert find_max_cpu_load(jobs) == ans

# Test Case 3
jobs, ans = [(1, 4, 2), (2, 4, 1), (3, 6, 5)], 8
assert find_max_cpu_load(jobs) == ans
```

### Solution

```python
from heapq import heappop, heappush

def find_max_cpu_load(jobs):
    load_changes = []
    for job in jobs:
        start, cpu_load, end = job
        heappush(load_changes, (start, cpu_load))
        heappush(load_changes, (end, -cpu_load))
    if not load_changes:
        return 0

    max_load, load = 0, 0
    while load_changes:
        t, new_load = heappop(load_changes)
        load += new_load
        while load_changes and load_changes[0][0] == t:
            _, new_load = heappop(load_changes)
            load += new_load
        max_load = max(max_load, load)
    return max_load
```
