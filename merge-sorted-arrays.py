# Chanantaphon Chanuksri (Man) 095-503-3632
import heapq

def merge_sorted_arrays(arr):
    heap, result = [], []
    l = 0
    
    while l < len(arr):
        # if the array is not empty
        if arr[l]:
            # push element to the heap with time complexity O(log m)
            heapq.heappush(heap, [arr[l][0], l, 0])
        l += 1
    
    while heap:
        # pop the root element from the heap with time complexity O(log m)
        min_arr = heapq.heappop(heap)
        # minimum number
        min_num = min_arr[0]
        # index of the array
        idx_arr = min_arr[1]
        # pointer index of the number in the array
        ptr_num = min_arr[2] 

        # add the minimum number to the result
        result.append(min_num)

        if ptr_num < len(arr[idx_arr]) - 1:
            # add the next element to the heap with time complexity O(log m)
            heapq.heappush(heap, [arr[idx_arr][ptr_num + 1], idx_arr, ptr_num + 1])
  
    return result
    
    # n = number of arrays
    # m = number of elements in the sub array
    # Total time complexity: O(n log m + m log m) = O(n log m)
    # Total space complexity: O(m + n) = O(n)


if __name__ == "__main__":
    assert merge_sorted_arrays([[10, 10, 10], [10, 10], [10]]) == [10, 10, 10, 10, 10, 10]
    assert merge_sorted_arrays([[1, 3, 5], [2, 3], [2, 3, 5, 8]]) == [1, 2, 2, 3, 3, 3, 5, 5, 8]
    assert merge_sorted_arrays([[100, 300, 500], [20, 33], [24, 37, 53, 82]]) == [20, 24, 33, 37, 53, 82, 100, 300, 500]
    assert merge_sorted_arrays([[], [], []]) == []
    assert merge_sorted_arrays([[6], [], []]) == [6]
    assert merge_sorted_arrays([[], [6], []]) == [6]
    assert merge_sorted_arrays([[], [], [6]]) == [6]
    assert merge_sorted_arrays([[2], [3], [1]]) == [1, 2, 3]
    assert merge_sorted_arrays([[10, 11, 20], [100], [1]]) == [1, 10, 11, 20, 100]
    print("All tests passed!!")
