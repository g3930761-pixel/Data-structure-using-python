def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
            print("pass",i+1,":",arr)
        return arr
n = int(input("Enter no of elements:"))
arr = []
for i in range(n):
    element = int(input("Enter element:"))
    arr.append(element)
print("\noriginal array:",arr)
sorted_array = bubble_sort(arr)
print("\nsorted array in ascending order:",sorted_array)
