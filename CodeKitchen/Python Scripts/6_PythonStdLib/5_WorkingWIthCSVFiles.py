# CSV Files  csv  = comma separated values.
# Like a simplified spread sheet stored as a plaintext file.
import csv


# ===================== WRITING/CREATING CSV FILES ================================
# can not use Path class here as csv class's writer method needs a file as input.

# with open("Data.csv", "w", newline="") as file:
#     writer = csv.writer(file)
#     writer.writerow(["transaction_id", "product_id", "price"])
#     writer.writerow([1000, 1, 5])
#     writer.writerow([1001, 2, 20])

# in call to open(), added attribute : newline="" ,
# as while writing row, extra newline character was added after each row.

# ===================== READING CSV FILES ==========================================

with open("Data.csv") as file:  # Open files in read mode.
    reader = csv.reader(file)
    # print(list(reader))  # prints everything inside csv as string.
    for row in reader:
        print(row)
    # we will not see the output of above  for-loop in terminal,
    # it is because the index of reader object which is initially at the start of the file comes to end of the file after iterating once,
    # when we converted reader to list an iteration was performed internally, hence on continuing iteration in for loop, nothing was printed.
    # so lets comment line 22 and check. (we get rows , each being an array of strings.)
