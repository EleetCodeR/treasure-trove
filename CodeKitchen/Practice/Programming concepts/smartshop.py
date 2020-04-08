if __name__ == '__main__':
    test_input = int(input())
    llist = []
    for _ in range(test_input):
        n = input()
        i = 0
        b = len(n)-1
        while(i < b):
            if (n[i] > n[i+1]):
                break
            i = i+1
        llist.append(int(n[0:i]+n[i+1:]))
    for price in llist:
        print(price)
