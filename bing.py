import pandas as pd
import json

with open('mini_data.json', 'r') as f:
    data = json.load(f)

try:
    cs_ceny = pd.json_normalize(data['Data']['cs_ceny'])
    cs_var_list = pd.json_normalize(data['Data']['cs_var_list'])
    merged_table = pd.merge(cs_ceny, cs_var_list, on='produkty')
    print(merged_table)
except ValueError as e:
    print("Error reading JSON:", e)