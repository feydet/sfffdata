import pandas as pd
melb_df = pd.read_csv("C:\IDE\melbourn\melb_data_fe\melb_data_fe.csv")
print(melb_df.groupby('Rooms')[['Price', 'BuildingArea']].median())
print(melb_df.groupby(['Rooms', 'Type'])['Price'].mean())
print(melb_df.groupby(['Rooms', 'Type'])['Price'].mean().unstack())
print(melb_df.pivot_table(
    values='Price',
    index='Rooms',
    columns='Type',
    fill_value=0
).round())
print(melb_df.pivot_table(
    values='Price',
    index='Regionname',
    columns='Weekend',
    aggfunc='count'
))
print(melb_df.pivot_table(
    values='Landsize',
    index='Regionname',
    columns='Type',
    aggfunc=['median', 'mean'],
    fill_value=0
))
print(melb_df.pivot_table(
    values='Price',
    index=['Method','Type'],
    columns='Regionname',
    aggfunc='median',
    fill_value=0
))

pivot = melb_df.pivot_table(
    values='Price',
    index='SellerG',
    columns='Type',
    aggfunc='median',
)
max_unit_price = pivot['unit'].max()
print(pivot[pivot['unit'] == max_unit_price].index[0])