# Merge K Lists

## Example Problem: Merge k Sorted Lists

_Original Problem:_ [_LeetCode #23 (Hard)_](https://leetcode.com/problems/merge-k-sorted-lists/)__

You are given an array of `k` linked lists `lists`, each linked list is sorted in ascending order.

Merge all the linked lists into one sorted linked list and return it.

### Starter Code

```python
def merge_k_lists(heads):
    """Takes an array of heads of sorted linked lists, returns merged sorted linked list"""
    pass 
```

### Solution

```python
from heapq import heappop, heappush
    
def merge_k_lists(heads):
    min_heap = []
    for head in heads:
        if head:
            heappush(min_heap, (head.val, id(head), head))  
    curr = new_head = ListNode(0)
    while min_heap:
        _, _, head = heappop(min_heap)
        curr.next = head
        head = head.next
        curr = curr.next
        curr.next = None
        if head:
            heappush(min_heap, (head.val, id(head), head))
    return new_head.next
```

