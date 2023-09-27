import pandas as pd

df = pd.read_csv('big-mac-full-index.csv')
# #row of min value of bigmac
# idx_min = df['dollar_price'].idxmin()

# print(df.loc[idx_min][1]) #returns series(loc, locates the row and returns)
year = 2012
query_t = f"( date == {year})"
df_result = df.query(query_t)

x = df_result['dollar_price'].median()

print(x)
# idx_min = df['dollar_price'].idxmin()
# # loc_code = df.loc[idx_min][1]
# # loc_name = df.loc[idx_min][3]
# # loc_dlrPrice = df.loc[idx_min][6]
# print(idx_min)