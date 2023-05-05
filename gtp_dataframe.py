import pandas as pd
import json

# load the JSON file
with open('mini_data.json', 'r') as f:
    data = json.load(f)

# extract the required data from the JSON
cs_ceny = data['Data']['cs_ceny']
cs_var_list = data['Data']['cs_var_list']
cis_prod_list = data['Data']['cis_prod_list']

# create a list of dictionaries for each row in the table
rows = []
for cs in cs_var_list:
    for cena in cs_ceny:
        if cena['kod_cs'] == cs['kod_cs']:
            row = {
                'kod_cs': cena['kod_cs'],
                'telefon': cs['telefon'],
                'produkty': cs['produkty'],
                'sluzby': cs['sluzby'],
                'prezentace': cs['prezentace']['uziv_text'],
                'platnost_od_1': cs['provozni_doba'][0]['platnost_od'],
                'platnost_do_1': cs['provozni_doba'][0]['platnost_do'],
                'platnost_od_2': cs['provozni_doba'][1]['platnost_od'],
                'platnost_do_2': cs['provozni_doba'][1]['platnost_do'],
            }
            for c in cena['ceny']:
                row[f"cena_{c['kod_produkt']}"] = c['cena']
            rows.append(row)

# create a DataFrame from the list of dictionaries
df = pd.DataFrame(rows)

# replace empty lists with NaN
df = df.applymap(lambda x: x if x != [] else None)
