__author__ = 'sid'

# Stack Implementation Using Arrays (strings)


def push(stack):
    print "Enter the Item to be pushed: "
    item = input()

    # Add the Item
    stack.append(item)

    #Increment the pointer(first)
    return len(stack) - 1


def pop(stack):
    # delete the item referenced by first
    print "Item deleted: " + str(stack[len(stack) - 1])
    del stack[len(stack) - 1]

    #decrement thr pointer(first)
    return len(stack) - 1


def IsEmpty(stack):
    if len(stack) > 0:
        print "Stack is not empty"
    else:
        print "Stack is empty"


def main(stack):
    print "*******************************************"
    print "1. Check for Empty"
    print "2. Push"
    print "3. Pop"
    print "4. Show Stack"
    print "5. Exit"
    print "Enter your choice: "
    option = input()

    if option == 1:
        IsEmpty(stack)
    elif option == 2:
        first = push(stack)
        print "Pushed into the stack at index:" + str(first)
    elif option == 3:
        first = pop(stack)
        print "Popped out of the stack from index:" + str(first + 1)
    elif option == 4:
        print stack
    elif option == 5:
        exit(1)
    else:
        print "Wrong choice!!"


if __name__ == "__main__":
    # intialize a list(array)
    stack = []

    for i in range(1000):
        main(stack)
