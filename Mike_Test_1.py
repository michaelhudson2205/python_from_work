import pathlib
import re

import pandas as pd

my_directory = pathlib.Path("../maildir")

# my_directory.rglob("*")

# list(my_directory.rglob("*"))

emails = list(my_directory.glob("./*/*sent*/*"))
len(emails)


# file1 = open("../maildir_small/allen-p/sent/1")
# print(file1.read())
# file1.close()

# file1 = open(emails[1])
# print(file1.read())
# file1.close()

PATTERN_dt = "^Date: \w\w\w, (\d+ \w\w\w \d{4}) (\d\d:\d\d:\d\d)"

# re.search(PATTERN_dt, file1.read())

# Start Testing==========
re.search(PATTERN_dt, "Date: Tue, 5 Dec 2000 07:31:00 -0800 (PST)")
with open(emails[0]) as file:
    line = file.readline()
    line = file.readline()

print(line)
re.search(PATTERN_dt, line)
file.close()
# End Testing ==========

# Start of the good stuff ==========
enron_data = []
for email in emails:
    with open(email) as file:
        line = file.readline()
        line = file.readline()

    if re.search(PATTERN_dt, line):
        m1 = re.search(PATTERN_dt, line)
        enron_date = m1.group(1)
        enron_time = m1.group(2)

    # row_list = [enron_date, enron_time]
    # enron_data.append(row_list)

    file.close()

    lines = open(email, "r").readlines()
    count_worda = 0
    count_wordb = 0
    for a in lines:
        if re.search("fraud", a, re.IGNORECASE):
            count_worda += 1
        if re.search("bankrupt", a, re.IGNORECASE):
            count_wordb += 1
    # test_row_list = [count_worda, count_wordb]
    # test_list.append(test_row_list)

    row_list = [enron_date, enron_time, count_worda, count_wordb]
    enron_data.append(row_list)


# End of the good stuff ==========
len(enron_data)

enron_data[0]

# Got this working ==========
test_list = []
for email in emails:
    lines = open(email, "r").readlines()
    count_worda = 0
    count_wordb = 0
    for a in lines:
        if re.search("the", a, re.IGNORECASE):
            count_worda += 1
        if re.search("to", a, re.IGNORECASE):
            count_wordb
    test_row_list = [count_worda, count_wordb]
    test_list.append(test_row_list)
    # emails[i].close()

len(test_list)

enron_dt[3000]
len(enron_dt)
len(emails)

# Start More Testing ==========
lines = open(emails[0], "r").readlines()
lines
lines[1]

re.search(PATTERN_dt, lines[1])

count_word = 0
line_number = 0
for a in lines:
    line_number += 1
    if re.search("now", a, re.IGNORECASE):
        print(f"Yes, found on line {line_number}")
        count_word += 1
print(count_word)

df = pd.DataFrame(enron_data, columns=["Date", "Time", "F_count", "B_count"])
print(df)

df.dtypes

# print(enron_data)
Total_Fraud = df["F_count"].sum()
print(Total_Fraud)

Total_Bankrupt = df["B_count"].sum()
print(Total_Bankrupt)
