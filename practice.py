import pandas as pd

filename = "big-mac-full-index.csv"

df = pd.read_csv(filename)

# print(df)

# #print(df.columns) #important so you see what you can use

# print(type(df['dollar_price']))
# print(df['name'])


query_text = f"(iso_a3 == 'ARG')"

df_arg = df.query(query_text)

#print(df_arg)

#df_arg.to_csv('argentina_report.csv')

print(df_arg['dollar_price'].min())