import numpy as np

def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:
	#Write your code here and return a python list after reshaping by using numpy's tolist() method
	old_m, old_n = len(a),len(a[0])
	new_m, new_n = new_shape
	# check vaild
	if old_m*old_n != new_m*new_n:
		return []
	reshaped = []
	for i in range(new_m):
		reshaped.append([])
		for j in range(new_n):
			loc = i*new_n+j
			row = loc // old_n
			col = loc % old_n
			reshaped[i].append(a[row][col])
	reshaped_matrix = reshaped
	return reshaped_matrix