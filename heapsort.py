import math

# Prints values of an array 
def print_array(arr):
    string = ""
    for num in arr:
        string += str(num) + " "
    print string
    
def bubble_down(arr, i):
    # Base Cases:
    # 1. Reached end of tree
    # 2. arr[i] > arr[child nodes]
    #1. index of child nodes > max index of array
    if 2*i >= len(arr):
        return
    
    # 2. if only one child node - only check first child node
    elif 2*i+1 > len(arr):
        left_child = arr[2*i-1]
        if arr[i-1] > left_child:
            return
        else:
            # Swap values
            arr[2*i-1], arr[i-1] = (arr[i-1], arr[2*i-1]);
            
            # recursive call
            bubble_down(arr, 2*i);
        
    # 2. if two child nodes check both 
    elif arr[i-1] > arr[2*i-1] and arr[i-1] > arr[2*i]:
        return
        
    largest = max(arr[2*i-1], arr[2*i]);
    largest_id = arr.index(largest);
    
    # swap largest 
    arr[i-1], arr[largest_id] = largest, arr[i-1];
    bubble_down(arr, largest_id + 1);
    
    return arr;
        
    
    
def build_heap(arr):
    index = math.floor(len(arr)/2)
    
    while index >= 1:
        bubble_down(arr, int(index));
        index -= 1
        
    return arr

def delete_max(arr):
    # Swap first and last element
    last_id = len(arr) - 1
    arr[0], arr[last_id] = arr[last_id], arr[0]
    
    # delete last element (max elem)
    del arr[last_id];
    
    # bubble_down to get heap structure again 
    bubble_down(arr, 1)
    return arr

def heapsort(arr):
    sorted_array = [];
    for i in range(len(arr)):
        sorted_array.append(arr[0]);
        delete_max(arr);
        
    return sorted_array;

# Ask for user to input an array 
array = []

print "Enter 10 numbers to place in array";
for i in range(10):
    num = int(raw_input())
    array.append(num);

# Print the array
print "This is your array"
print_array(array);

# Build heap from array 
print "This is your heap array"
heap_array = build_heap(array);
print_array(heap_array);

# sort array using heap sort 
print "This is your sorted array"
sorted_array = heapsort(heap_array);
print_array(sorted_array);