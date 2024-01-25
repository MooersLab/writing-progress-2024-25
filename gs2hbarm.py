import gspread
import pandas as pd
import matplotlib.pyplot as plt

gc = gspread.oauth()
sh = gc.open('wp-2024-25')

# Checking connection
# print(sh.worksheet("min_day").get('H1:AE1'))
# print(sh.worksheet("min_day").get('H733:AE733'))

"""
Plot cumulative hours per project from Google Sheet workbook as horizontal bar plot.
Must authorize access to Google Sheets and Google Drive first time.
This authorization is done only once.

Blaine Mooers and OU Board of Regents
OUHSC
2024 January 25
"""

# Fetch the project names to plotted on Y-axis.
P = sh.worksheet("min_day").get('H1:AE1')

projects = [
    x
    for xs in P
    for x in xs
] 

# Minutes were converted to hours in the spreadsheet.
H = sh.worksheet("min_day").get('H733:AE733')


# We get a list of lists of strings from gspread.
# We have to flatten to a list.
hours =  [
    x
    for xs in H
    for x in xs
] 

# Convert the strings in our list into floats.
float_list = list(map(float, hours))   



# plot y,x
plt.barh(projects, float_list)

# setting x-label as pen sold
plt.xlabel("Hours")

# setting y_label as price
plt.ylabel("Project Name")

plt.rcParams.update({'font.size': 8})

# If project name is long, shift the plot frame to the right.
plt.subplots_adjust(left=0.28)
plt.show()

#plt.savefig('gs2barh.pdf', dpi=100)
