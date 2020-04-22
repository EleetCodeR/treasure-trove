if __name__ == "__main__":
    count = int(input())
    seq = list(map(int, input().rstrip().split()))

    seq.sort()
    maxKey = 0
    for i in range(count):
        if i == count-1:
            break

        key = seq[i] % seq[i+1]
        if(maxKey < key):
            maxKey = key

    print(maxKey)
