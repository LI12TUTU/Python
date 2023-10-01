import numpy as np
import pandas as pd
import math

# 读入数据集，假设文件名为ratings.csv，包含'user_id', 'movie_id', 'rating'三列
ratings = pd.read_csv('ratings.csv', sep='\t', encoding='latin-1', usecols=['user_id', 'movie_id', 'rating'])
# 生成用户评分矩阵，行为用户，列为电影，值为评分，缺失值用0填充
user_movie_ratings = ratings.pivot_table(index='user_id', columns='movie_id', values='rating', fill_value=0)
# 选取前20个用户的数据作为测试
test_ratings = user_movie_ratings.head(20)
print(test_ratings)

user_count = test_ratings.shape[0]
# print(user_count)

# 用户相似度矩阵
user_sim_matrix = pd.DataFrame(np.zeros((user_count, user_count)), index=np.arange(1, user_count + 1),
															 columns=np.arange(1, user_count + 1))


# print(user_sim_matrix)

# 计算向量内积
def dot_product(user_u_vec, user_v_vec):
	res = 0
	for i in user_u_vec.index:
		res += user_u_vec[i] * user_v_vec[i]
	return res


# print(user_movie_ratings.loc[1], user_movie_ratings.loc[2])
# print(dot_product(user_movie_ratings.loc[1], user_movie_ratings.loc[2]))

# 计算向量模长
def calc_vec_norm(vec):
	res = 0
	for i in vec.index:
		res += vec[i] * vec[i]
	return math.sqrt(res)


# print(calc_vec_norm(user_movie_ratings.loc[1]))

def calc_user_sim(rating_matrix, sim_matrix):
	for user_u in rating_matrix.index:
		for user_v in rating_matrix.index:
			if user_u == user_v:
				continue
			# 计算用户向量的内积
			uv_dot_product = dot_product(rating_matrix.loc[user_u], rating_matrix.loc[user_v])
			# 计算用户向量的模长
			u_norm = calc_vec_norm(rating_matrix.loc[user_u])
			v_norm = calc_vec_norm(rating_matrix.loc[user_v])
			# 计算用户之间的相似度
			sim_matrix.loc[user_u, user_v] = uv_dot_product / (u_norm * v_norm)

# 计算相似度矩阵
calc_user_sim(test_ratings, user_sim_matrix)
print(user_sim_matrix)


def recommend(rating_matrix, sim_matrix, user_u, K, N):
	# 找到目标用户u的相似度最高的K个用户
	sim_users = sim_matrix.loc[user_u].sort_values(ascending=False)[0:K]
	print(sim_users)
	rank = pd.Series(np.zeros((rating_matrix.shape[1],)), index=rating_matrix.columns)

	for user in sim_users.index:
		for movie in rating_matrix.columns:
			# 目标用户已经看过这部电影
			if rating_matrix.loc[user_u][movie] != 0:
				continue
			if rating_matrix.loc[user][movie] != 0:
				# 计算相似用户对物品的评分以及和目标用户之间的相似度的乘积
				sim_factor = sim_matrix.loc[user_u, user] * rating_matrix.loc[user][movie]
				# 累加K个用户，得到物品的加权和作为目标用户的预测评分
				rank[movie] += sim_factor

	print(rank)
	recommend_list = list(rank.sort_values(ascending=False)[0:N].index)
	return recommend_list


# 测试推荐，为用户1推荐20部电影
rec_list = recommend(test_ratings, user_sim_matrix, 1, 10, 20)
print(rec_list)
