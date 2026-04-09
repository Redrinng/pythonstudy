# import requests

# import csv

# r = requests.get('https://api.census.gov/data/2020/acs/acs5?get=NAME,B08303_001E,B08303_013E&for=county:*&in=state:36')

# r_json = r.json()

# with open("commute_data.csv", mode="w", newline="") as commute_data:
#   writer = csv.writer(commute_data)
#   writer.writerows(r.json())


import pandas

commute_df = pandas.read_csv("commute_data.csv")

# Rename DataFrame colunms
commute_df.columns = ["name", "total commuters", "total hours commuted", "state", "county"]

# Preview DataFrame
print(commute_df.head())