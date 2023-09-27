import pandas as pd
big_mac_file = './big-mac-full-index.csv'

df = pd.read_csv(big_mac_file)

def get_big_mac_price_by_year(year,country_code):
    query_t = f"(iso_a3 == '{country_code.upper()}' or date == '{year}')"
    df_result = df.query(query_t)
    mean_dllr = round(df_result['dollar_price'].mean(),2)
    return mean_dllr

def get_big_mac_price_by_country(country_code):
    query_t = f"(iso_a3 == '{country_code.upper()}')"
    df_result = df.query(query_t)
    mean_dllr = round(df_result['dollar_price'].mean(),2)
    return mean_dllr

def get_the_cheapest_big_mac_price_by_year(year):
    query_t = f"(date >= '{year}-01-01' and date <= '{year}-12-31')"
    df_result = df.query(query_t)
    idx_min = df_result['dollar_price'].idxmin()
    chepeast_bm = df_result.loc[idx_min]
    return f"{chepeast_bm['name']}({chepeast_bm['iso_a3']}):{round(chepeast_bm['dollar_price'],1)}"

def get_the_most_expensive_big_mac_price_by_year(year):
    query_t = f"(date >= '{year}-01-01' and date <= '{year}-12-31')"
    df_result = df.query(query_t)
    idx_max = df_result['dollar_price'].idxmax()
    chepeast_bm = df_result.loc[idx_max]
    return f"{chepeast_bm['name']}({chepeast_bm['iso_a3']}):{round(chepeast_bm['dollar_price'],1)}"

if __name__ == "__main__":
    c = 'arg'
    yr = 2003
    # print(get_big_mac_price_by_year(yr,c))
    # print("\n")
    # print(get_big_mac_price_by_country(c))
    print(get_the_most_expensive_big_mac_price_by_year(yr))
    pass