def execute(cmd):
    l = []
    for c in cmd:
        if(c[0] == "insert"):
            l.insert(int(c[1]), int(c[2]))

        if(c[0] == "print"):
            print(l)

        if(c[0] == "remove"):
            l.remove(int(c[1]))

        if(c[0] == "append"):
            l.append(int(c[1]))

        if(c[0] == "sort"):
            l.sort()

        if(c[0] == "pop"):
            l.pop()

        if(c[0] == "reverse"):
            l.reverse()


if __name__ == '__main__':
    N = int(input())
    cmd = []
    for _ in range(N):
        cmd.append(list(input().strip().split()))

    execute(cmd)
