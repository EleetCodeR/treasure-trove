def runnerUp(score):
    # Remove duplicates
    score = set(score)
    # Remove highest score
    score.remove(max(score))
    return (max(score))


if __name__ == "__main__":
    n = int(input())
    score = list(map(int, input().rstrip().split()))

    if(2 <= n <= 10):
        print(runnerUp(score))
