import pandas as pd
import json
import sys

# Load JSON data into a Python dictionary
with open('mini_data.json') as f:
    data = json.load(f)

# Extract relevant information from the dictionary
cs_ceny = data['Data']['cs_ceny']
print(type(cs_ceny))
print(cs_ceny)
sys.exit()
cs_var_list = data['Data']['cs_var_list']
cis_prod_list = data['Data']['cis_prod_list']

# Create an empty DataFrame to hold the combined information
columns = ['kod_cs', 'telefon', 'prezentace', 'produkty', 'provozni_doba', 'cena_1', 'cena_4', 'cena_9', 'cena_11']
df = pd.DataFrame(columns=columns)

# Iterate through the cs_var_list items and fill in the DataFrame
for cs_var in cs_var_list:
    try:  
        row = {
            'kod_cs': cs_var['kod_cs'],
            'telefon': cs_var['telefon'],
            'prezentace': cs_var['prezentace']['uziv_text'],
            'produkty': '|'.join(cs_var['produkty']),
            #'provozni_doba': '|'.join(['{}:{}-{}'.format(pd['platnost_od'], pd['po'], pd['ne']) for pd in cs_var['provozni_doba']]),
        }
    except KeyError:
        continue

    # Iterate through the cs_ceny items to fill in the row with prices
    for cs_cena in cs_ceny:
        if cs_cena['kod_cs'] == cs_var['kod_cs']:
            for cena in cs_cena['ceny']:
                if cena['kod_produkt'] == '1':
                    row['cena_1'] = cena['cena']
                elif cena['kod_produkt'] == '4':
                    row['cena_4'] = cena['cena']
                elif cena['kod_produkt'] == '9':
                    row['cena_9'] = cena['cena']
                elif cena['kod_produkt'] == '11':
                    row['cena_11'] = cena['cena']
    df = df.append(row, ignore_index=True)

# Iterate through the cis_prod_list items and add columns for each product
for cis_prod in cis_prod_list:
    df[cis_prod['nazev_produkt']] = ''

# Iterate through the rows of the DataFrame and fill in the product columns
for i, row in df.iterrows():
    for cis_prod in cis_prod_list:
        kod_produkt = cis_prod['kod_produkt']
        for produkt in row['produkty'].split('|'):
            if kod_produkt == produkt:
                df.at[i, cis_prod['nazev_produkt']] = 'x'

# Fill any missing values with empty strings
df = df.fillna('')

# Print the final DataFrame
print(df)

df.to_excel('my_data.xlsx', index=True)
