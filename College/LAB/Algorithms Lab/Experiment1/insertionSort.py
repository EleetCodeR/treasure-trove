import os
import time
inStart, inStop, fileReadST, fileReadSTP, fileWriteST, fileWriteSTP = 0, 0, 0, 0, 0, 0
insST_75K, insST_150K, insST_300K, insST_450K = 0, 0, 0, 0
insSTP_75K, insSTP_150K, insSTP_300K, insSTP_450K = 0, 0, 0, 0


def inSort(flist):
    for j in range(1, len(flist)):
        key = flist[j]
        i = j-1
        while(i >= 0 and flist[i] > key):
            flist[i+1] = flist[i]
            i = i-1
        flist[i+1] = key


def inMain():
    global inStart, inStop, insST_75K, insST_150K, insST_300K, insST_450K, insSTP_75K, insSTP_150K, insSTP_300K, insSTP_450K, fileReadST, fileReadSTP, fileWriteST, fileWriteSTP
    inStart = time.time()

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

    insST_75K = time.time()
    inSort(file1_Data)
    insSTP_75K = time.time()
    print("insertion-sort @ 75K: %s sec" % (insSTP_75K-insST_75K))

    inSort(file2_Data)
    inSort(file3_Data)
    inSort(file4_Data)
    inSort(file5_Data)
    inSort(file6_Data)

    file7_Data = file1_Data + file2_Data
    insST_150K = time.time()
    inSort(file7_Data)
    insSTP_150K = time.time()
    print("insertion-sort @ 150K: %s sec" % (insSTP_150K-insST_150K))

    file8_Data = file3_Data + file4_Data
    inSort(file8_Data)

    file9_Data = file5_Data + file6_Data
    inSort(file9_Data)

    file10_Data = file7_Data + file8_Data
    insST_300K = time.time()
    inSort(file10_Data)
    insSTP_300K = time.time()
    print("insertion-sort @ 300K: %s sec" % (insSTP_300K-insST_300K))

    # This is the main sorted file
    file11_Data = file9_Data + file10_Data
    insST_450K = time.time()
    inSort(file11_Data)
    insSTP_450K = time.time()
    print("insertion-sort @ 450K: %s sec" % (insSTP_450K-insST_450K))

    fileWriteST = time.time()
    os.remove("elementsFile.txt")
    with open("elementsFile.txt", "w") as file:
        for item in file11_Data:
            file.write("%s\n" % item)
    file.close()
    fileWriteSTP = time.time()
    print("file-write: %s sec" % (fileWriteSTP-fileWriteST))

    inStop = time.time()
    print("insertion Sort : %s sec" % (inStop-inStart))
