
# ========= BRUTE FORCE ============= #
# def arrayManipulation(n, queries):
#     zeros = [0]*n

#     for query in queries:
#         a = query[0]
#         b = query[1]
#         k = query[2]
#         try:
#             i = queries.index(query, 0, 0)
#         except ValueError:
#             i = -1

#         if(1 <= a <= n and 1 <= b <= n and 0 <= k <= 10**9):
#             for i in range(a-1, b):
#                 zeros[i] = zeros[i]+k

#     zeros.sort(reverse=True)
#     return zeros[0]

# ========= Better  ============= #


def arrayManipulation(n, queries):
    zeros = [0]*n
    for z in queries:
        zeros[z[0] - 1] += z[2]
        if z[1] != len(zeros):
            zeros[z[1]] -= z[2]
    maxval = 0
    val = 0

    for z in zeros:
        val += z
        if val > maxval:
            maxval = val

    return maxval


if __name__ == '__main__':

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    if((3 <= n <= 10**5) and (1 <= m <= 2*(10**5))):
        queries = []

        for _ in range(m):
            queries.append(list(map(int, input().rstrip().split())))

        result = arrayManipulation(n, queries)
        print(result)
