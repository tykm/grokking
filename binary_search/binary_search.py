from generate_ordered_array import generate

ordered_array = generate(100000000)
#print(ordered_array)

print("starting")
def binary_search_iter(arr: list[int], target: int):
    low = 0
    high = len(arr) - 1
    guess_index = (low + high) // 2
    guess = arr[guess_index]
    
    while guess != target:
        if guess > target:
            high = guess_index - 1
        else:
            low = guess_index + 1
        guess_index = (high + low) // 2
        guess = arr[guess_index]
    return guess
    
             
print(binary_search_iter(ordered_array, 90000000))
i = 0
num = ordered_array[i]
while num != 90000000:
    i+=1
    num = ordered_array[i]
print(num)
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