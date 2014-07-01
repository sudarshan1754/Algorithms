__author__ = 'sid'

# Selection Sort Algorithm Implementation
# No. of compares = (N ^ 2)/2
# No. of exchanges = N
# Complexity: Quadratic (N ^ 2)


# Function to compare (takes (N ^ 2)/2 compares)
def compare(i, j):
    if i < j:
        return True
    else:
        return False


# Function to perform exchange (takes N exchanges)
def exchange(arr, i, min):
    temp = arr[i]
    arr[i] = arr[min]
    arr[min] = temp

    print i + 1, arr


# Function to get the Items from user
def GetItems():
    print "Enter the Number of Elements: "
    N = input()
    arr = []
    print "Enter the Numbers: "
    for i in range(N):
        arr.append(input())

    return arr


#Function to perform selection sort
def SelectionSort():
    arr = GetItems()
    print "\nOriginal Order"
    print arr
    print "\nAfter Applying Selection Sort\nItn. Order"

    # Iterate over each i and get the index of the min item
    for i in range(len(arr)):
        min = i
        for j in range(i + 1, len(arr)):
            if compare(arr[j], arr[min]):
                min = j
        exchange(arr, i, min)


if __name__ == "__main__":
    SelectionSort()

