import pathlib
import re

import pandas as pd

my_directory = pathlib.Path("../maildir")

emails = list(my_directory.glob("./*/*sent*/*"))

PATTERN_dt = "^Date: \w\w\w, (\d+ \w\w\w \d{4}) (\d\d:\d\d:\d\d)"

enron_data = []
for email in emails:
    with open(email) as file:
        line = file.readline()
        line = file.readline()

    if re.search(PATTERN_dt, line):
        m1 = re.search(PATTERN_dt, line)
        enron_date = m1.group(1)
        enron_time = m1.group(2)

    file.close()

    lines = open(email, "r").readlines()
    count_worda = 0
    count_wordb = 0
    for a in lines:
        if re.search("fraud", a, re.IGNORECASE):
            count_worda += 1
        if re.search("bankrupt", a, re.IGNORECASE):
            count_wordb += 1

    row_list = [enron_date, enron_time, count_worda, count_wordb]
    enron_data.append(row_list)

len(enron_data)

df = pd.DataFrame(enron_data, columns=["Date", "Time", "F_count", "B_count"])
print(df)

df.dtypes

Total_Fraud = df["F_count"].sum()
print(Total_Fraud)

Total_Bankrupt = df["B_count"].sum()
print(Total_Bankrupt)
