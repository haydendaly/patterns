---
description: >-
  https://github.com/haydendaly/experiments/blob/main/patterns/fast_and_slow_pointers.ipynb
---

# Fast and Slow Pointers

## What are fast and slow pointers?

The Fast & Slow pointer approach, also known as the Hare & Tortoise algorithm, is a pointer algorithm that uses two pointers which move through the array (or sequence/Linked List) at different speeds. This approach is quite useful when dealing with cyclic Linked Lists or arrays.

## Example Problem: Linked List Cycle

_Original Problem:_ [_LeetCode #141_](https://leetcode.com/problems/linked-list-cycle/)__

Given the head of a Singly Linked __ List, write a function to determine if the Linked List has a cycle in it or not.

### Starter Code

```python
def has_cycle(head):
    """Takes in head of Linked List, returns boolean of whether a cycle is present"""
    pass

# Test Case 1
head = Node(1)
head.next = Node(2)
head.next.next = head
assert has_cycle(head)

# Test Case 2
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
assert not has_cycle(head)
```

### Solution

```python
def has_cycle(head):
    slow, fast = head, head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        if slow == fast:
            return True
    return False
```

By moving references at different speeds, the algorithm proves that the two pointers are bound to meet if they ever equal one another.
