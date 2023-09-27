# import pandas as pd

# df = pd.read_csv('big-mac-full-index.csv')

# # query = f"(iso_a3 == 'NZL' or iso_a3 == 'DNK')"

# # df_result = df.query(query)

# # mean_dllr_price = df_result['dollar_price'].mean()

# # mean_dllr_price_two_dec = round(mean_dllr_price,2)##ROUND FOR ASSIGNMENT

# # print(mean_dllr_price)
# # print(mean_dllr_price_two_dec)

# # print(df_result['dollar_price'].min())
# # print(df_result['dollar_price'].max())
# # print(df_result['dollar_price'].mean())
# # print(round(df_result['dollar_price'].median(),2))


# ##

# year = '2017'
# country_code = 'ARG'
# ###YYYY-MM-DD
# new_query = f"date >= '{year}-01-0/1' and date <= '{year}-12-31' and iso_a3 == {country_code}"

# #call a data frame , df

# df_by_date = df.query(new_query)
# print(df_by_date)