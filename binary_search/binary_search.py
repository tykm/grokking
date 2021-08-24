from generate_ordered_array import generate

ordered_array = generate(8)
print(ordered_array)

def binary_search_iter(arr: list[int], target: int):
    low = 0
    high = len(arr) - 1
    mid = (low + high) // 2
    while arr[mid] != target:
        if arr[mid] < target:
            low = mid + 1
            mid = (low + high) // 2
        elif arr[mid] > target:
            high = mid - 1
            mid = (low + high) // 2
    return(arr[mid])
    
             
print(binary_search_iter(ordered_array, 3))

'''
Cases:
Array Even:
    Target Lower:
        Target Even:
            arr = 8
            target = 2
        Target Odd:
            arr = 8
            target = 3


Array Odd:











'''