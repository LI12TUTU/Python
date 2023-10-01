import pandas as pd

data = pd.read_csv("../ratings.csv", sep="\t",  usecols=['user_id', 'movie_id', 'rating'])
print(data)
# print(data.index, data.columns)

dataset = pd.read_csv("../MovieRecommendation-master/ml-latest-small/ratings.csv",
											usecols=["userId", "movieId", "rating"])
ratings = dataset.pivot_table(index='userId', columns='movieId', values='rating', fill_value=0)
print(dataset)
print(ratings)