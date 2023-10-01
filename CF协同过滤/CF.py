rating_file = "D:\\Python\\CF协同过滤\\MovieRecommendation-master\\ml-latest-small\\ratings.csv"


def get_row_and_column(filename):
	user_set = set()
	movie_set = set()

	with open(filename, "r") as file:
		for i, line in enumerate(file):
			if i == 0:
				continue
			user, movie, rating, timestamp = line.strip("\r\n").split(",")
			user_set.add(user)
			movie_set.add(movie)
	return len(user_set), len(movie_set)


def get_dataset(filename, matrix):
	with open(filename, "r") as file:
		for i, line in enumerate(file):
			if i == 0:
				continue
			user, movie, rating, timestamp = line.strip("\r\n").split(",")

			user = int(user)
			movie = int(movie)
			rating = float(rating)
			if user > 610 or movie > 9724:
				print(user, movie)

			# matrix[user][movie] = rating


row, column = get_row_and_column(rating_file)
print(row, column)

# 二维数组 表示用户评价矩阵 索引为0的第一行第一列舍弃不用
data_matrix = [list() for i in range(row + 1)]
for i in range(1, row + 1):
	data_matrix[i] = [0 for j in range(column + 1)]
print(data_matrix[0], len(data_matrix[1]))

get_dataset(rating_file, data_matrix)
print(data_matrix[1])