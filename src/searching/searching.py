def linear_search(arr, target):
   	for i in range(len(arr)):
   		if arr[i] == target:
   			return i 
   	return -1


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
	min = 0
	max = len(arr)
	while (min + max) // 2:
		i = (min + max) // 2
		if arr[i] == target:
			return i
		elif target < arr[i]:
			max = i
		else:
			min = i + 1
	return -1
