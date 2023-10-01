class Node:
	value = 0
	left_child = None
	right_child = None

	def __init__(self, value):
		self.value = value

def create_tree(nums):
	length = len(nums)
	if length == 0:
		return None

	max_el = max(nums)
	max_el_index = nums.index(max_el)
	root = Node(max_el)

	if length == 1:
		return root
	# 处理左子表
	root.left_child = create_tree(nums[0:max_el_index])
	# 处理右子表
	root.right_child = create_tree(nums[max_el_index + 1:length])

	return root


def visit_tree(root):
	if root:
		print(root.value, end=" ")
		if root.left_child is None and root.right_child is None:
			return
		visit_tree(root.left_child)
		visit_tree(root.right_child)
	else:
		print("null", end=" ")


nums = [int(num) for num in input().split()]
root_node = create_tree(nums)
visit_tree(root_node)
