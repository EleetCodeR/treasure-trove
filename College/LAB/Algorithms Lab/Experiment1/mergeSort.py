import os
import time
mrgStart, mrgStop, fileReadST, fileReadSTP, fileWriteST, fileWriteSTP = 0, 0, 0, 0, 0, 0
msST_75K, msST_150K, msST_300K, msST_450K = 0, 0, 0, 0
msSTP_75K, msSTP_150K, msSTP_300K, msSTP_450K = 0, 0, 0, 0


def merge(left, right):
    if not len(left) or not len(right):
        return left or right

    result = []
    i, j = 0, 0
    while (len(result) < len(left) + len(right)):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
        if i == len(left) or j == len(right):
            result.extend(left[i:] or right[j:])
            break

    return result


def mergeSort(list):
    if len(list) < 2:
        return list

    middle = len(list)//2
    left = mergeSort(list[:middle])
    right = mergeSort(list[middle:])

    return merge(left, right)


def mergeMain():
    global mrgStart, mrgStop, msST_75K, msST_150K, msST_300K, msST_450K, msSTP_75K, msSTP_150K, msSTP_300K, msSTP_450K, fileReadST, fileReadSTP, fileWriteST, fileWriteSTP
    mrgStart = time.time()

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

    msST_75K = time.time()
    file1_Data = mergeSort(file1_Data)
    msSTP_75K = time.time()
    print("merge-sort @ 75K: %s sec" % (msSTP_75K-msST_75K))

    file2_Data = mergeSort(file2_Data)
    file3_Data = mergeSort(file3_Data)
    file4_Data = mergeSort(file4_Data)
    file5_Data = mergeSort(file5_Data)
    file6_Data = mergeSort(file6_Data)

    file7_Data = file1_Data + file2_Data
    msST_150K = time.time()
    file7_Data = mergeSort(file7_Data)
    msSTP_150K = time.time()
    print("merge-sort @ 150K: %s sec" % (msSTP_150K-msST_150K))

    file8_Data = file3_Data + file4_Data
    file8_Data = mergeSort(file8_Data)

    file9_Data = file5_Data + file6_Data
    file9_Data = mergeSort(file9_Data)

    file10_Data = file7_Data + file8_Data
    msST_300K = time.time()
    file10_Data = mergeSort(file10_Data)
    msSTP_300K = time.time()
    print("merge-sort @ 300K: %s sec" % (msSTP_300K-msST_300K))

    # This is the main sorted file
    file11_Data = file9_Data + file10_Data
    msST_450K = time.time()
    file11_Data = mergeSort(file11_Data)
    msSTP_450K = time.time()
    print("merge-sort @ 450K: %s sec" % (msSTP_450K-msST_450K))

    fileWriteST = time.time()
    os.remove("elementsFile.txt")
    with open("elementsFile.txt", "w") as file:
        for item in file11_Data:
            file.write("%s\n" % item)
    file.close()
    fileWriteSTP = time.time()
    print("file-write: %s sec" % (fileWriteSTP-fileWriteST))

    mrgStop = time.time()
    print("merge Sort : %s sec" % (mrgStop-mrgStart))

# # Driver code
# a = [12, 11, 13, 5, 6, 7,15,200,22,64,128,229,500,11,12,10,55,250,2,0,15,20,420,2500]
# print("Given array is ")
# print(a)
# print("Sorted array is ")
# print(mergeSort(a))
