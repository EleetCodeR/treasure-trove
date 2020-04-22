def secondLast(data):
    scores = [d[1] for d in data]
    mn = min(scores)
    while (mn in scores):
        scores.remove(mn)
    mn = min(scores)
    names = []
    for d in data:
        if(d[1] == mn):
            names.append(d[0])

    if len(names) > 1:
        names.sort()

    for name in names:
        print(name)


if __name__ == "__main__":
    data = list()
    for _ in range(int(input())):
        name = input()
        score = float(input())
        data.append([name, score])

    secondLast(data)
