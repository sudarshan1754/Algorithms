__author__ = 'sid'

# Shell Sort Algorithm Implementation (Variation of Insertion Sort)
# No. of compares = ~(N ^ 3/2) (Avg.) Theoretical with Knuth's 3x + 1 series
# Complexity: (N ^ 2) (Worst case)
"""
Series:
    Shell's : 2's power - 1
    Knuth's : 3x + 1
    Sedgewick
"""

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


# Function to perform Shell sort
def ShellSort():
    arr = GetItems()
    print "\nOriginal Order"
    print arr
    print "\nAfter Applying Shell Sort"

    h = 1
    while h < len(arr) / 3:
        # Knuth's (3X + 1), that is 1, 4 13, 40......
        h = 3 * h + 1

    while h >= 1:
        for i in xrange(h, len(arr)):
            for j in xrange(i, h - 1, -h):
                if compare(arr[j], arr[j - h]):
                    exchange(arr, j, j - h)
        h /= 3


if __name__ == "__main__":
    ShellSort()

