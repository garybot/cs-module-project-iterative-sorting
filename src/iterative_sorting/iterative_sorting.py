# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # find next smallest element
        for j in range(cur_index, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j
        # swap
        arr[cur_index], arr[smallest_index]  = arr[smallest_index], arr[cur_index]
        # increment
        cur_index += 1
        smallest_index = cur_index

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    swapped = True
    cur_index = 0
    while swapped:
        swapped = False
        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True
        cur_index += 1

    return arr

'''
STRETCH: implement the Counting Sort function below

Counting sort is a sorting algorithm that works on a set of data where
we specifically know the maximum value that can exist in that set of
data. The idea behind this algorithm then is that we can create "buckets"
from 0 up to the max value. This is most easily done by initializing an
array of 0s whose length is the max value + 1 (why do we need this "+ 1"?).

Each buckets[i] then is responsible for keeping track of how many times 
we've seen `i` in the input set of data as we iterate through it.
Once we know exactly how many times each piece of data in the input set
showed up, we can construct a sorted set of the input data from the 
buckets. 

What is the time and space complexity of the counting sort algorithm? Bad
'''
def counting_sort(arr, maximum=None):
    # Your code here
    buckets = []
    if maximum:
        buckets = [0 for x in range(maximum + 1)]

    for val in arr:
        buckets[val] += 1

    for i in range(len(buckets) - 1):
        buckets[i + 1] += buckets[i]

    new_arr = [None for x in range(len(arr))];
    for x in arr:
        buckets[x] -= 1
        new_arr[buckets[x]] = x

    return new_arr

counting_sort([1,2,3,4,2,2,1,5], 5);