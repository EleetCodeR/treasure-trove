import matplotlib.pyplot as plt
import random
import time

from quickSort import qMain
from insertionSort import inMain
from mergeSort import mergeMain
from heapSort import heapMain

ioStart = 0
ioStop = 0


def initialize():
    global ioStart
    ioStart = time.time()
    # Generate random elements and populate the file.
    elements_List = []
    for i in range(450000):
        elements_List.append(random.randint(0, 450000))

    with open("elementsFile.txt", "w") as file:
        for item in elements_List:
            file.write("%s\n" % item)
    file.close()


def distributeIntoFiles():
    global ioStop, ioStart
    # Read all the elements from the file
    main_List = []
    with open("elementsFile.txt", "r") as file:
        data = file.read().splitlines()
        for index in range(450000):
            main_List.append(data[index])
        file.close()

    # Distributing elements into files
    file1_Data = main_List[0:75000]
    file2_Data = main_List[75000:150000]
    file3_Data = main_List[150000:225000]
    file4_Data = main_List[225000:300000]
    file5_Data = main_List[300000:375000]
    file6_Data = main_List[375000:450000]

    with open("file1.txt", "w") as file1, open("file2.txt", "w") as file2, open("file3.txt", "w") as file3, open("file4.txt", "w") as file4, open("file5.txt", "w") as file5, open("file6.txt", "w") as file6:
        for item in range(75000):
            file1.write("%s\n" % file1_Data[item])
            file2.write("%s\n" % file2_Data[item])
            file3.write("%s\n" % file3_Data[item])
            file4.write("%s\n" % file4_Data[item])
            file5.write("%s\n" % file5_Data[item])
            file6.write("%s\n" % file6_Data[item])
    file1.close()
    file2.close()
    file3.close()
    file4.close()
    file5.close()
    file6.close()

    ioStop = time.time()
    print("file-IO : %s sec" % (ioStop-ioStart))


# ======/ Start /==========
# initialize()
# distributeIntoFiles()

# =======/ Sort /===========
# qMain()
# file-IO : 1.746917963027954 sec
# file-read: 0.1252460479736328 sec
# quick-sort @ 75K: 0.3150804042816162 sec
# quick-sort @ 150K: 1251.5158021450043 sec
# quick-sort @ 300K: 5166.1403465271 sec
# quick-sort @ 450K: 16741.623969316483 sec
# file-write: 0.485642671585083 sec
# quick Sort : 25628.38157081604 sec

# inMain()
# file-IO : 1.6812107563018799 sec
# file-read: 0.14064455032348633 sec
# insertion-sort @ 75K: 276.90327620506287 sec
# insertion-sort @ 150K: 477.14451360702515 sec
# insertion-sort @ 300K: 2067.7035613059998 sec
# insertion-sort @ 450K: 4202.520514965057 sec
# file-write: 0.86069655418396 sec
# insertn Sort : 9167.682001829147 sec

# mergeMain()
# file-IO : 1.618579387664795 sec
# file-read: 0.1262195110321045 sec
# merge-sort @ 75K: 0.7471017837524414 sec
# merge-sort @ 150K: 0.9213299751281738 sec
# merge-sort @ 300K: 1.7997877597808838 sec
# merge-sort @ 450K: 3.0163838863372803 sec
# file-write: 0.5027754306793213 sec
# merge Sort : 12.636591672897339 sec

# heapMain()
# file-IO : 1.7293572425842285 sec
# file-read: 0.13265013694763184 sec
# heapSort @ 75K: 0.6652429103851318 sec
# heapSort @ 150K: 1.2357196807861328 sec
# heapSort @ 300K: 2.6718218326568604 sec
# heapSort @ 450K: 4.254646301269531 sec
# file-write: 0.5226011276245117 sec
# heapSort : 15.292101621627808 sec

# ================================/ Graph Plots /===================
x = [75000, 150000, 300000, 450000]
y_Qs = [0.3150804042816162, 1251.5158021450043,
        5166.1403465271, 16741.623969316483]
y_Ins = [276.90327620506287, 477.14451360702515,
         2067.7035613059998, 4202.520514965057]
y_Mrgs = [0.7471017837524414, 0.9213299751281738,
          1.7997877597808838, 3.0163838863372803]
y_Hps = [0.6652429103851318, 1.2357196807861328,
         2.6718218326568604, 4.254646301269531]

plt.xticks(x)
# plt.plot(x, y_Qs, 'o-b', label='Quick Sort')
# plt.plot(x, y_Ins, 'o-r', label='Insertion Sort')
# plt.plot(x, y_Mrgs, 'o-g', label='Merge Sort')
plt.plot(x, y_Qs, 'v:',  ms='6', label='Quick Sort')
plt.plot(x, y_Ins, 'o:',  ms='4.5', label='Insertion Sort')
plt.plot(x, y_Mrgs, 'd-.', ms='6', linewidth=4, label='Merge Sort')
plt.plot(x, y_Hps, 'o-', ms='3', label='Heap Sort')
plt.xlabel('Number of elements')
plt.ylabel('Running Time (sec)')
plt.title("Time Complexity Of Sorting Algorithms")
plt.legend()
plt.show()
