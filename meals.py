import pandas as pd
import datetime

""" The File needs to have duplicates removed and prepped for reading"""


df = pd.read_excel(r"C:\Users\kyle.anderson\Documents\PACS - Meal Penalty Upload\*.xlsx")

df = df.drop(columns = 'reference (delete column)')
building_range = df['Company ID']

list_of_unique_buildings = set(building_range)


for building in list_of_unique_buildings:
    result_df = df[df['Company ID'] == building]
    result_df.to_csv(fr'C:\Users\kyle.anderson\Documents\Meal_penalties_export\{building}.csv', index = False)
