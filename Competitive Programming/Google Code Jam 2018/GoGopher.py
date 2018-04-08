import sys
t = int(input())

for _ in range(t):
    A = int(input())
    n = A//3
    n += int(bool(A%3))
    L = []
    n = max(n, 3)
    for x in range(n):
        L.append([False, False, False])

    flag = [False]*n
    solved = False
    unsolved = False
    #print L

    while False in flag:

        for x in range(n):
            if flag[x] == False:
                if x==n-1:
                    print (8+x, 10)
                elif x==0:
                    print (10, 10)
                else:
                    print (9+x, 10)
                sys.stdout.flush()

                i, j = list(map(int, input().split()))
                if i==j and i==0:
                    solved = True
                    break

                if i==j and i==-1:
                    unsolved = True
                    break

                L[i-9][j-9] = True
                if L[i-9][0] and L[i-9][1] and L[i-9][2]:
                    flag[i-9] = True

        if solved or unsolved:
            break




    if unsolved:
        break
