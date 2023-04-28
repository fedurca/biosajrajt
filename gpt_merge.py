import json
import pandas as pd
import sys

# Load the JSON schema file
with open('cepro_schema.json') as f:
    schema = json.load(f)

#print(schema) 

#sys.exit()

# Load the JSON data file
with open('cepro_data.json') as f:
    data = json.load(f)

# Extract the root object from the schema
root_object = schema['Data'].keys()[0]

# Extract the data corresponding to the root object
root_data = data[root_object]

# Convert the root data to a pandas DataFrame
df = pd.DataFrame(root_data)

# Print the resulting DataFrame
print(df)