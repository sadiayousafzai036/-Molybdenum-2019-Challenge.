def goldenLeader(A):
    n = len(A)
    size = 0
    for k in range(n):
        if (size == 0):
            size += 1
            value = A[k]
        else:
            if (value != A[k]):
                size -= 1
            else:
                size += 1
    candidate = -1
    if (size > 0):
        candidate = value
    leader = -1
    count = 0
    for k in range(n):
        if (A[k] == candidate):
            count += 1
    if (count > n // 2):
        leader = candidate
    if leader>0:
        return leader
    else:
        None

def maxleader(A,M,K,counter):
    N=[]
    i=0
    z=K-1
    while z<len(A):
        B = []
        B = A.copy()
        for j in range(i,K+i):
            B[j] = A[j] + 1
        number=goldenLeader(B)
        if number not in N and number is not None:
            N.append(number)
        i+=1
        z+=1
    return N
def solution(K, M, A):
    # write your code in Python 3.6
    global number
    global N
    number=0
    counter=0
    for i in range(0,len(A)):
        if A[i]>M:
            return []
    N=maxleader(A,M,K,counter)
    N.sort()
    return N





print(solution(1, 1, [1]))

#print(solution(4,2,[1,2,2,1,2]))