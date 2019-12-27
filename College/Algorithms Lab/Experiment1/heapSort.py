import os
import time
hsStart, hsStop, fileReadST, fileReadSTP, fileWriteST, fileWriteSTP = 0, 0, 0, 0, 0, 0
hsST_75K, hsST_150K, hsST_300K, hsST_450K = 0, 0, 0, 0
hsSTP_75K, hsSTP_150K, hsSTP_300K, hsSTP_450K = 0, 0, 0, 0

# Python program for implementation of heap Sort

# To heapify subtree rooted at index i.
# n is size of heap


def heapify(arr, n, i):
    largest = i  # Initialize largest as root
    l = 2 * i + 1	 # left = 2*i + 1
    r = 2 * i + 2	 # right = 2*i + 2

    # See if left child of root exists and is
    # greater than root
    if l < n and arr[i] < arr[l]:
        largest = l

    # See if right child of root exists and is
    # greater than root
    if r < n and arr[largest] < arr[r]:
        largest = r

    # Change root, if needed
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # swap

        # Heapify the root.
        heapify(arr, n, largest)

# The main function to sort an array of given size


def heapSort(arr):
    n = len(arr)

    # Build a maxheap.
    for i in range(n, -1, -1):
        heapify(arr, n, i)

    # One by one extract elements
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # swap
        heapify(arr, i, 0)


def heapMain():
    global hsStart, hsStop, fileReadST, fileReadSTP, fileWriteST, fileWriteSTP, hsST_75K, hsST_150K, hsST_300K, hsST_450K, hsSTP_75K, hsSTP_150K, hsSTP_300K, hsSTP_450K
    hsStart = time.time()

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

    hsST_75K = time.time()
    heapSort(file1_Data)
    hsSTP_75K = time.time()
    print("heapSort @ 75K: %s sec" % (hsSTP_75K-hsST_75K))

    heapSort(file2_Data)
    heapSort(file3_Data)
    heapSort(file4_Data)
    heapSort(file5_Data)
    heapSort(file6_Data)

    file7_Data = []
    file7_Data = file1_Data + file2_Data
    hsST_150K = time.time()
    heapSort(file7_Data)
    hsSTP_150K = time.time()
    print("heapSort @ 150K: %s sec" % (hsSTP_150K-hsST_150K))

    file8_Data = file3_Data + file4_Data
    heapSort(file8_Data)

    file9_Data = file5_Data + file6_Data
    heapSort(file9_Data)

    file10_Data = file7_Data + file8_Data
    hsST_300K = time.time()
    heapSort(file10_Data)
    hsSTP_300K = time.time()
    print("heapSort @ 300K: %s sec" % (hsSTP_300K-hsST_300K))

    # This is the main sorted file
    file11_Data = file9_Data + file10_Data
    hsST_450K = time.time()
    heapSort(file11_Data)
    hsSTP_450K = time.time()
    print("heapSort @ 450K: %s sec" % (hsSTP_450K-hsST_450K))

    fileWriteST = time.time()
    os.remove("elementsFile.txt")
    with open("elementsFile.txt", "w") as file:
        for item in file11_Data:
            file.write("%s\n" % item)
    file.close()
    fileWriteSTP = time.time()
    print("file-write: %s sec" % (fileWriteSTP-fileWriteST))

    hsStop = time.time()
    print("heapSort : %s sec" % (hsStop-hsStart))
