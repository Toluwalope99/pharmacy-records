#-------------------------------------------------------------------------------
# Name:        pharmaco
# Purpose:
#
# Author:      Toluwalope
#
# Created:     18/06/2022
# Copyright:   (c) Akly 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import os
import pandas
from difflib import SequenceMatcher
import csv

current_path = os.chdir(r"C:\Users\Akly\Desktop")

first = 'DB_Data.csv'
second = 'Test_Data.csv'

main_file = pandas.read_csv(first, keep_default_na=False, dtype={
                        'Dosage': str,})

test_file = pandas.read_csv(second, keep_default_na=False)

x = len(main_file)
y = len(test_file)

main_headers = list(main_file)
test_headers = list(test_file)


main_list = []

count = 0
while count < x:
    temp_list = []
    temp_list.append(main_file[main_headers[2]][count])
    temp_list.append(main_file[main_headers[3]][count])
    temp_list.append(main_file[main_headers[4]][count])
    count += 1
    main_list.append(temp_list)

test_list = []

count = 0
while count < y:
    temp_list = []
    temp_list.append(test_file[test_headers[0]][count])
    count += 1
    test_list.append(temp_list)

compare_main = []

for item in main_list:
    temp = item[0] + item[1] + item[2]
    compare_main.append(temp.replace(' ', ''))

compare_test = [item[0].replace(' ', '') for item in test_list]

positions = []
for item in compare_test:
    temp = []
    for value in compare_main:
        ratio = SequenceMatcher(None, value, item).ratio()
        temp.append(ratio)
    highest = max(temp)
    position = temp.index(highest)
    positions.append(position)

##print(len(positions))

final_list = []

new_headers = ['Medicine Code', 'Trade Name', 'Form', 'Dosage', 'Excl Price']

final_list.append(new_headers)

count = 0
while count < y:
    temp_list = []
    temp_list.append(main_file[main_headers[0]][positions[count]])
    temp_list.append(main_file[main_headers[2]][positions[count]])
    temp_list.append(main_file[main_headers[3]][positions[count]])
    temp_list.append(main_file[main_headers[4]][positions[count]])
    temp_list.append(test_file[test_headers[1]][count])
    count += 1
    final_list.append(temp_list)

with open('Compared.csv', 'w', newline='') as file:
    writer = csv.writer(file, quoting = csv.QUOTE_ALL)
    writer.writerows(final_list)

print('DONE')

