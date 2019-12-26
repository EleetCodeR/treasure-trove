import os
import time
qsStart, qsStop, fileReadST, fileReadSTP, fileWriteST, fileWriteSTP = 0, 0, 0, 0, 0, 0
qsST_75K, qsST_150K, qsST_300K, qsST_450K = 0, 0, 0, 0
qsSTP_75K, qsSTP_150K, qsSTP_300K, qsSTP_450K = 0, 0, 0, 0


def qPartition(flist, l, h):
    pivot = flist[h]
    i = l-1
    for j in range(l, h):
        if flist[j] <= pivot:
            i = i+1
            flist[i], flist[j] = flist[j], flist[i]

    flist[i+1], flist[h] = flist[h], flist[i+1]
    return i+1


# def quickSort(flist, l, h):
#     if l < h:
#         pi = qPartition(flist, l, h)
#         quickSort(flist, l, pi-1)
#         quickSort(flist, pi+1, h)

def quickSort(flist, low, high):
    # Create an auxiliary stack
    size = high - low + 1
    stack = [0] * (size)

    # initialize top of stack
    top = -1

    # push initial values of l and h to stack
    top = top + 1
    stack[top] = low
    top = top + 1
    stack[top] = high

    # Keep popping from stack while is not empty
    while top >= 0:

        # Pop h and l
        high = stack[top]
        top = top - 1
        low = stack[top]
        top = top - 1

        # Set pivot element at its correct position in sorted array
        p = qPartition(flist, low, high)

        # If there are elements on left side of pivot,
        # then push left side to stack
        if p-1 > low:
            top = top + 1
            stack[top] = low
            top = top + 1
            stack[top] = p - 1

        # If there are elements on right side of pivot,
        # then push right side to stack
        if p+1 < high:
            top = top + 1
            stack[top] = p + 1
            top = top + 1
            stack[top] = high


# # test
# arr = [65, 70, 75, 80, 85, 60, 55, 50, 45]
# n = len(arr)
# quickSort(arr, 0, n-1)
# print(f"SORTED:{arr}")


def qMain():
    global qsStart, qsStop, qsST_75K, qsST_150K, qsST_300K, qsST_450K, qsSTP_75K, qsSTP_150K, qsSTP_300K, qsSTP_450K, fileReadST, fileReadSTP, fileWriteST, fileWriteSTP
    qsStart = time.time()

    fileReadST = time.time()
    file1_Data = []
    file2_Data = []
    file3_Data = []
    file4_Data = []
    file5_Data = []
    file6_Data = []

    with open("file1.txt", "r") as file1, open("file1.txt", "r") as file2, open("file3.txt", "r") as file3, open("file4.txt", "r") as file4, open("file5.txt", "r") as file5, open("file6.txt", "r") as file6:
        file1_Data = file1.read().splitlines()
        file1_Data = list(map(int, file1_Data))

        file2_Data = file2.read().splitlines()
        file2_Data = list(map(int, file2_Data))

        file3_Data = file3.read().splitlines()
        file3_Data = list(map(int, file3_Data))

        file4_Data = file4.read().splitlines()
        file4_Data = list(map(int, file4_Data))

        file5_Data = file5.read().splitlines()
        file5_Data = list(map(int, file5_Data))

        file6_Data = file6.read().splitlines()
        file6_Data = list(map(int, file6_Data))

        file1.close()
        file2.close()
        file3.close()
        file4.close()
        file5.close()
        file6.close()

        os.remove("file1.txt")
        os.remove("file2.txt")
        os.remove("file3.txt")
        os.remove("file4.txt")
        os.remove("file5.txt")
        os.remove("file6.txt")

    fileReadSTP = time.time()
    print("file-read: %s sec" % (fileReadSTP-fileReadST))

    qsST_75K = time.time()
    quickSort(file1_Data, 0, 75000-1)
    qsSTP_75K = time.time()
    print("quick-sort @ 75K: %s sec" % (qsSTP_75K-qsST_75K))

    quickSort(file2_Data, 0, 75000-1)
    quickSort(file3_Data, 0, 75000-1)
    quickSort(file4_Data, 0, 75000-1)
    quickSort(file5_Data, 0, 75000-1)
    quickSort(file6_Data, 0, 75000-1)

    file7_Data = []
    file7_Data = file1_Data + file2_Data
    qsST_150K = time.time()
    quickSort(file7_Data, 0, 150000-1)
    qsSTP_150K = time.time()
    print("quick-sort @ 150K: %s sec" % (qsSTP_150K-qsST_150K))

    file8_Data = file3_Data + file4_Data
    quickSort(file8_Data, 0, 150000-1)

    file9_Data = file5_Data + file6_Data
    quickSort(file9_Data, 0, 150000-1)

    file10_Data = file7_Data + file8_Data
    qsST_300K = time.time()
    quickSort(file10_Data, 0, 300000-1)
    qsSTP_300K = time.time()
    print("quick-sort @ 300K: %s sec" % (qsSTP_300K-qsST_300K))

    # This is the main sorted file
    file11_Data = file9_Data + file10_Data
    qsST_450K = time.time()
    quickSort(file11_Data, 0, 450000-1)
    qsSTP_450K = time.time()
    print("quick-sort @ 450K: %s sec" % (qsSTP_450K-qsST_450K))

    fileWriteST = time.time()
    os.remove("elementsFile.txt")
    with open("elementsFile.txt", "w") as file:
        for item in file11_Data:
            file.write("%s\n" % item)
    file.close()
    fileWriteSTP = time.time()
    print("file-write: %s sec" % (fileWriteSTP-fileWriteST))

    qsStop = time.time()
    print("quick Sort : %s sec" % (qsStop-qsStart))
