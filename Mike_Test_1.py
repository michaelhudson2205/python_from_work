import pathlib
import re

import pandas as pd

my_directory = pathlib.Path("../maildir")

interest = [
    "allen-p",
    "arnold-j",
    "arora-h",
    "bass-e",
    "beck-s",
    "brawner-s",
    "buy-r",
    "campbell-l",
    "dasovich-j",
    "delainey-d",
    "derrick-j",
    "farmer-d",
    "gay-r",
    "geaccone-t",
    "germany-c",
    "giron-d",
    "grigsby-m",
    "haedicke-m",
    "hodge-j",
    "jones-t",
    "kaminski-v",
    "kean-s",
    "kuykendall-t",
    "lokay-m",
    "lokey-t",
    "love-p",
    "mann-k",
    "martin-t",
    "may-l",
    "mckay-b",
    "mclaughlin-e",
    "neal-s",
    "nemec-g",
    "pereira-s",
    "perlingiere-d",
    "presto-k",
    "ring-a",
    "rogers-b",
    "sager-e",
    "sanders-r",
    "shackleton-s",
    "shankman-j",
    "shively-h",
    "sturm-f",
    "taylor-m",
    "tholt-j",
    "townsend-j",
    "weldon-c",
    "white-s",
]

len(interest)
emails = []

for i in interest:
    get_one = list(my_directory.glob(f"./{i}/*sent*/*"))
    emails.append(get_one)

# get_one = list(my_directory.glob(f"./weldon-c/*sent*/*"))
# emails.append(get_one)

len(emails)
# emails[40]

flatList = []
flatList = [element for innerList in emails for element in innerList]
len(flatList)
# flatList[82452]


# emails = list(my_directory.glob("./*/*sent*/*"))

# PATTERN_dt = "^Date: \w\w\w, (\d+ \w\w\w \d{4}) (\d\d:\d\d:\d\d)"
PATTERN_dt = "^Date: \w\w\w, (\d+ \w\w\w \d{4} \d\d:\d\d:\d\d)"

enron_data = []
for e in flatList:
    with open(e) as file:
        line = file.readline()
        line = file.readline()

    if re.search(PATTERN_dt, line):
        m1 = re.search(PATTERN_dt, line)
        enron_date = m1.group(1)
        # enron_time = m1.group(2)

    file.close()

    lines = open(e, "r").readlines()
    count_worda = 0
    count_wordb = 0
    for a in lines:
        if re.search("fraud", a, re.IGNORECASE):
            count_worda += 1
        if re.search("bankrupt", a, re.IGNORECASE):
            count_wordb += 1

    # row_list = [enron_date, enron_time, count_worda, count_wordb]
    row_list = [enron_date, count_worda, count_wordb]
    enron_data.append(row_list)

len(enron_data)

# df = pd.DataFrame(enron_data, columns=["Date", "Time", "F_count", "B_count"])
df = pd.DataFrame(enron_data, columns=["DateTime", "F_count", "B_count"])
# print(df)

# df.dtypes

# Total_Fraud = df["F_count"].sum()
# print(Total_Fraud)

# Total_Bankrupt = df["B_count"].sum()
# print(Total_Bankrupt)

# convert Date column from string to date
# df.dtypes
# df["DateTime"] = pd.to_datetime(df["DateTime"])
# df.dtypes
# df['Time'] = pd.to_datetime(df['Time'], format='%H:%M')
# df.dtypes
# df


df.to_csv("unfiltered_82452.csv")

# Filtering to get the emails sent outside of "normal" hours 9am - 5pm.
# df.set_index("DateTime").between_time("17:00", "9:00").reset_index()
