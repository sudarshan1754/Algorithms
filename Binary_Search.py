__author__ = 'sid'

# Binary Search Algorithm
# Complexity: O(log N)

def BinarySearch(Number_list, key):
    low = 0
    high = len(Number_list) - 1

    while low <= high:
        mid = low + (high - low) / 2

        if key < Number_list[mid]:
            high = mid - 1
        elif key > Number_list[mid]:
            low = mid + 1
        else:
            return mid

    return -1


def main():
    print "Enter the Number of Elements: "
    n = input()

    print "Enter the elements one after the other:"
    Number_list = []
    for i in range(n):
        num = input()
        Number_list.append(num)

    # Sort the list in Ascending order, Note: This time isn't part of complexity mentioned above
    Number_list.sort()

    print "Enter the Key to be searched: "
    key = input()

    index = BinarySearch(Number_list, key)

    if index == -1:
        print "Key not found"
    else:
        print "Key found at index: " + str(index)

if __name__ == "__main__":
    main()