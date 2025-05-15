""" Binary Search is the algorithm that searches sorted lists of 'n' elements by looking at the middle section and then reducing it by half, repeatedly, while looking for a specific target. In the worst case scenario, for a list of n elements, it would take n steps to find the target element. Binary search would only take log2 n steps to to it. This difference in steps (O(log n) x O(n)) is called Big O Notation."""

def binary_search(array,item): # Sorted array!
    low = 0 # Index
    high = len(array) - 1 # Index
    steps = 1
    
    while low <= high:
        mid = (low + high) // 2 # Index
        guess = array[mid] # Guessed item from the array; NOT INDEX!
        if guess == item:
            print(f"Number of steps: {steps}")
            return mid
        if guess < item:
            low = mid + 1
        else: # guess > item
            high = mid - 1
        steps += 1
    
    print(f"Number of steps: {steps}")
    return None

numbers = [1,3,7,11] # 1 to 4
chosen_number = 7

print(f"\nThe index of the chosen element is: {binary_search(numbers, chosen_number)}\n")

numbers = list(range(1,240001)) # 1 to 240000
chosen_number = 240000

print(f"\nThe index of the chosen element is: {binary_search(numbers, chosen_number)}\n")

# Also valid for searching elements that do not belong in the array.