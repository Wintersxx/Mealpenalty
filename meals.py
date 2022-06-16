import pandas as pd
import datetime
import os

""" The File needs to have duplicates removed and prepped for reading"""

# A file path on YOUR computer works best. Onedrive will block it.
date = date.today()

# Creating the upload file path. New date for each Penalty upload
if not os.path.exists(fr"C:\Users\kyle.anderson\Documents\PACS_Meals_Upload\ {date}_mp"):
    os.makedirs(fr"C:\Users\kyle.anderson\Documents\PACS_Meals_Upload\ {date}_mp")
# Hardcoded excel file needs to be saved here
df = pd.read_excel(fr"C:\Users\kyle.anderson\Documents\PACS_Meals_Upload\*")

df = df.drop(columns='facname (delete column)')
df = df.drop(columns='reference (delete column)')
building_range = df['Company ID']

list_of_unique_buildings = set(building_range)

for building in list_of_unique_buildings:
    result_df = df[df['Company ID'] == building]
    result_df.to_csv(fr"C:\Users\kyle.anderson\Documents\PACS_Meals_Upload\ {date}_mp\{building}.csv", index = False)
