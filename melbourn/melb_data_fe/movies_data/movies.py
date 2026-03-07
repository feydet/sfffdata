import pandas as pd
ratings1 = pd.read_csv(r"C:\IDE\melbourn\melb_data_fe\movies_data\ratings1.csv")
ratings2 = pd.read_csv(r"C:\IDE\melbourn\melb_data_fe\movies_data\ratings2.csv")
dates = pd.read_csv(r"C:\IDE\melbourn\melb_data_fe\movies_data\dates.csv")
movies = pd.read_csv(r"C:\IDE\melbourn\melb_data_fe\movies_data\movies.csv")
ratings = pd.concat([ratings1, ratings2])
print(ratings)
ratings = pd.concat(
    [ratings1, ratings2],
    ignore_index=True
)
print(ratings)
print('Число строк в таблице ratings: ', ratings.shape[0])
print('Число строк в таблице dates: ', dates.shape[0])
print(ratings.shape[0] == dates.shape[0])
ratings = ratings.drop_duplicates(ignore_index=True)
print('Число строк в таблице ratings: ', ratings.shape[0])
ratings_dates = pd.concat([ratings, dates], axis=1)
print(ratings_dates.tail(7))
joined_false = ratings_dates.join(
    movies,
    rsuffix='_right',
    how='left'
)
print(joined_false)
#joined = ratings_dates.join(
    #movies.set_index('movieId'),
    #on='movieId',
    #how='left'
#)
#print(joined.head())
merged = ratings_dates.merge(
    movies,
    on='movieId',
    how='left'
)
print(merged.head())
print('Число строк в таблице ratings_dates: ', ratings_dates.shape[0])
print('Число строк в таблице merged: ', merged.shape[0])
print(ratings_dates.shape[0] == merged.shape[0])
merged2 = ratings_dates.merge(
    movies,
    on='movieId',
    how='outer'
)
print('Число строк в таблице merged2: ', merged2.shape[0])
print(merged2.tail())
merge_ratings = ratings1.merge(ratings2, how='outer')
print('Число строк в таблице merge_ratings: ', merge_ratings.shape[0])
print(merge_ratings)