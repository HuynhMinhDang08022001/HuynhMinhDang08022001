import pandas
import openpyxl
import binascii
from openpyxl import Workbook
import numpy as np
import csv

with open('RFvalue.csv','r') as value_file:
    reader = csv.reader(value_file)
    with open('TC_RF.csv','w') as tc_file:
        writer = csv.writer(tc_file)
    count = 0

    for row in reader:
        print (row)

        if count > 5:
            break
        count += 1




# print(value[0])

# print(" ".join([hex(ch)[2:]  for line in value for ch in line]))
# String = ""
# for i in str(value):
#     String += hex(ord(i))[2:]
# print(String)




