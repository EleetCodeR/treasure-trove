

# Complete the hourglassSum function below.


def hourglassSum(arr):
    hr_sum = []
    for i in range(4):
        for j in range(4):
            a = arr[i][j]
            b = arr[i][j+1]
            c = arr[i][j+2]
            d = arr[i+1][j+1]
            e = arr[i+2][j]
            f = arr[i+2][j+1]
            g = arr[i+2][j+2]
            hr_sum.append(a+b+c+d+e+f+g)

    hr_sum.sort(reverse=True)

    return hr_sum[0]


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)
    print(result)
    # fptr.write(str(result) + '\n')

    # fptr.close()
