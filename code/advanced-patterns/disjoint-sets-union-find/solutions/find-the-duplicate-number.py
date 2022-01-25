def find_duplicate(nums): 
    for num in nums: 
        if nums[abs(num) - 1] < 0: 
            return abs(num) 
        nums[abs(num) - 1] *= -1 
    return -1

if __name__ == "__main__":
    nums = [1, 3, 4, 2, 2]
    result = 2
    assert find_duplicate(nums) == result

    nums = [3, 1, 3, 4, 2]
    result = 3
    assert find_duplicate(nums) == result
