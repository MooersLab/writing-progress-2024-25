import gspread
import pandas as pd
import matplotlib.pyplot as plt

"""
Plot cumulative words per project from Google Sheet workbook as horizontal bar plot.
Must authorize access to Google Sheets and Google Drive first time.
This authorization is done only once.

Blaine Mooers and OU Board of Regents
OUHSC
2024 January 25
"""

# gc = gspread.oauth()
# sh = gc.open('wp-2024-25')

gc = gspread.service_account()
sh = gc.open('wp-ja-2024-25')

#print(sh.worksheet("min_day").get('H1:AE1'))
#print(sh.worksheet("min_day").get('H733:AE733'))


P = sh.worksheet("word_day").get('I1:AE1')

# Flatten list of lists into a list of strings of project names
projects = [
    x
    for xs in P
    for x in xs
] 

H = sh.worksheet("word_day").get('I733:AE733')

hours =  [
    x
    for xs in H
    for x in xs
] 

# Convert the strings in our list into integers.
int_list = list(map(int, hours))   


# plot y,x
plt.barh(projects, int_list)

# setting x-label
plt.xlabel("Words")

# setting y_label
plt.ylabel("Project Name")

plt.rcParams.update({'font.size': 10})

# If project name is long, shift the plot frame to the right.
plt.subplots_adjust(left=0.15)

#plt.savefig('gshbarw.png', dpi=100)

plt.show()
