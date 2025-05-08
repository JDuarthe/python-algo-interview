# Time Complexity: O(n)
def two_sum(target: int, nums: list)-> list[int]|None:
    if len(nums) == 0:
        return None
    
    seen = {}

    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return sorted([seen[complement], i])
        seen[num] = i
    
    return None


def main():
    nums1 = [3, 2, 4]
    target1 = 6

    nums2 = [1, 7, 5, 2]
    target2 = 9

    nums3 = []
    target3 = 5

    print(two_sum(target1, nums1))
    print(two_sum(target2, nums2))
    print(two_sum(target3, nums3))


if __name__ == "__main__":
    main()