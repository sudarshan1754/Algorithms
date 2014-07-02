__author__ = 'sid'

# Insertion Sort Algorithm Implementation
# No. of compares = ~(N ^ 2)/4 (Avg.)
# No. of exchanges = ~(N ^ 2)/4 (Avg.)
# Complexity: (N ^ 2) (Worst case - Descending ordered)
#           : (N - 1) (Best Case - Already Sorted)


# Function to compare (Similar to selection sort)
def compare(i, j):
    if i < j:
        return True
    else:
        return False


# Function to perform exchange (Similar to selection sort)
def exchange(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp

    print arr


# Function to get the Items from user
def GetItems():
    print "Enter the Number of Elements: "
    N = input()
    arr = []
    print "Enter the Numbers: "
    for i in xrange(N):
        arr.append(input())

    return arr


# Function to perform selection sort
def InsertionSort():
    arr = GetItems()
    print "\nOriginal Order"
    print arr
    print "\nAfter Applying Insertion Sort"

    # Iterate over each i and get the index of the min item
    for i in xrange(len(arr)):
        for j in xrange(i, 0, -1):
            if compare(arr[j], arr[j - 1]):
                exchange(arr, j, j - 1)


if __name__ == "__main__":
    InsertionSort()

