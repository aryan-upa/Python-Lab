# ls1 = [1,2,3,4,5,6]
# ls2 = [7,8,9,5,6,7]
# Print a list which applies bitwise and on elements of both list at same index and store
# the result in a new list, using only list comprehension.
# List will be entered by user at time of execution.

ls1 = list(map(int, input('Enter the data of ls1: ').split()))
ls2 = list(map(int, input('Enter the data of ls2: ').split()))
ls = [a&b for (a,b) in zip(ls1,ls2)]
print(ls)