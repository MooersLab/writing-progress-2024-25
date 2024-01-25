# install gspread, calmap, calplot, vega_datasets with pip.
# I used Python 3.12.
import gspread
import calmap
import calplot
import pandas as pd
import numpy as np; np.random.seed(sum(map(ord, 'calplot')))
from vega_datasets import data as vds
import matplotlib.pyplot as plt

# You must enable access from your computer to your Google Sheets.
# See the read-the-doc for gspread.
gc = gspread.oauth()
sh = gc.open('wp-2024-25')

# Sanity check on the connection
# retrieve the date. This it the hard part.
#print(sh.worksheet("min_day").get('C1:C732'))

# retrieve the daily total time 
#print(sh.worksheet("min_day").get('E2:E732'))

# Generate a date range for next two years. 
# 2024 is a leap year with 366 days.
all_days = pd.date_range('1/1/2024', periods=731, freq='D')

# Fetch the daily minute total.
L = sh.worksheet("word_day").get('E2:E732')

# We get a list of lists of strings from gspread.
# We have to flatten to a list.

flat_list = [
    x
    for xs in L
    for x in xs
] 

# Convert the strings in our list into integers.
int_list = list(map(int, flat_list))   

# Make a pandas Series out of the list of integers with date as the index.
words = pd.Series(int_list, index=all_days)
#print(minutes.to_string())

calplot.calplot(words, cmap='Blues', figsize=(16,5.5));
plt.suptitle('Manuscript Writing Effort in Words per Day', y=1.0, fontsize=20);
plt.show()
