# Two sum with two pointers return 1-based index    
def two_sum_sorted(nums: list[int], target: int):
    left, right = 0, len(nums)-1
    
    while left < right:
        sum_number = nums[left] + nums[right]
        
        if sum_number == target:
            return [left+1, right+1]
        elif sum_number < target:
            left += 1
        else:
            right -= 1
    
    return None

def main():
    nums = [2, 7, 11, 15]
    target = 9
    print(two_sum_sorted(sorted(nums), target))

if __name__ == "__main__":
    main()