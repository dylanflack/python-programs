import time
import random

# Returns a list of numbers from 1 to 10000 in random order
def random_nums():
    nums = list(range(1, 10001))
    random.shuffle(nums)
    return nums


# Bubble Sort Algorithm
# Repeatedly compares and swaps adjacent elements until the list is sorted.
def bubble_sort(nums):
    n = len(nums)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]


# Merge Sort Algorithm
# Divides the list into halves, recursively sorts, and merges them.
def merge_sort(nums):
    if len(nums) > 1:
        mid = len(nums) // 2
        left = nums[:mid]
        right = nums[mid:]
        merge_sort(left)
        merge_sort(right)
        
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                nums[k] = left[i]
                i += 1
            else:
                nums[k] = right[j]
                j += 1
            k += 1
        
        while i < len(left):
            nums[k] = left[i]
            i += 1
            k += 1
        
        while j < len(right):
            nums[k] = right[j]
            j += 1
            k += 1


# Counting Sort Algorithm
# Counts occurrences of each element and reconstructs a sorted list.
def counting_sort(nums):
   
    max_val = max(nums)
    count = [0] * (max_val + 1)
    
    for num in nums:
        count[num] += 1
    
    sorted_nums = []
    for i in range(max_val + 1):
        sorted_nums.extend([i] * count[i])
    
    return sorted_nums


# Check if a list is sorted
def is_sorted(arr):
    return all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1))


# Main function
# Runs the algorithms and prints the timed results
def main():
    nums = random_nums()

    # Bubble Sort
    bubble_nums = nums.copy()
    start = time.time()

    bubble_sort(bubble_nums)
    end = time.time()

    # print results
    print(f"Bubble Sort: {'0' if is_sorted(bubble_nums) else '1'}")
    print(f"Time: {end - start}")


    # Merge Sort
    merge_nums = nums.copy()
    start = time.time()

    merge_sort(merge_nums)
    end = time.time()

    # print results
    print(f"\nMerge Sort: {'0' if is_sorted(merge_nums) else '1'}")
    print(f"Time: {end - start}")


    # Counting Sort
    counting_nums = nums.copy()
    start = time.time()

    counting_nums = counting_sort(counting_nums)
    end = time.time()

    # print results
    print(f"\nCounting Sort: {'0' if is_sorted(counting_nums) else '1'}")
    print(f"Time: {end - start}")


if __name__ == "__main__":
    main()
