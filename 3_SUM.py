__author__ = 'sid'

# 3-SUM Algorithm (Given N distinct integers, how many triples sum to exactly zero?)
# Method: Brute Force
# Complexity: (N ^ 3)
"""
# Measure the time by using Log-Log plot (Theoretical):
    POWER LAW: (a * N ^ b) where a = 2 ^ c
    that is: (1.006 * (10 ^ -10)) * (N ^ 2.999)
    plug in N in the above equation
"""


def GetCount(Numbers_list):
    Count = 0
    N = len(Numbers_list)
    for i in range(N):
        for j in range(i + 1, N):
            for k in range(j + 1, N):
                if Numbers_list[i] + Numbers_list[j] + Numbers_list[k] == 0:
                    Count += 1

    return Count


def main():
    print "Enter the No. of Numbers:"
    n = input()
    print "Get the Numbers:"
    Numbers_list = []
    for i in range(n):
        num = input()
        Numbers_list.append(num)

    print "Number of Sum's = 0 is : " + str(GetCount(Numbers_list))


if __name__ == "__main__":
    main()