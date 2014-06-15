__author__ = 'sid'

#Quick Find Algorithm Implementation
# 1. Initialize (N)
# 2. Find (1)
# 3. Union (N)
# Complexity : (N^2)

#Function to initialize the objects
def union_intialize(n):
    id_list = []

    for i in range(n):
        id_list.append(i)

    return id_list

#Find function to check if the objects are connected or not
def find(p, q):

    if id_list[p] == id_list[q]:
        return True
    else:
        return False

def union(id_list, p, q):
    pid = id_list[p]
    qid = id_list[q]

    for i in range(len(id_list)):
        if id_list[i] == pid:
            id_list[i] = qid

id_list = []
n = input('Enter the number of elements: ')
id_list = union_intialize(n)


#User Input
for i in range(1000):
    print "\n\n"
    print "1. To check if the objects are connected"
    print "2. Connect the objects"
    print "3. Print the list"
    print "4. Done"
    print "\nEnter your option: "
    option = input()

    if option == 1:
        #Get the Elements for which the connection is to be found
        p = input("Enter the First Object(No.): ")
        q = input("Enter the Second Object(No.): ")

        Result = find(p, q)

        #Spit out the result of the find connection
        if Result is False:
            print "\n**********Not Connected**********"
        else:
            print "\n**********Connected**********"

    if option == 2:
        #Get the Elements for which the connection is to be found
        p = input("Enter the First Object(No.): ")
        q = input("Enter the Second Object(No.): ")

        union(id_list, p, q)

        print "\n**********Success**********"

    if option == 3:
        print id_list

    if option == 4:
        exit(1)











