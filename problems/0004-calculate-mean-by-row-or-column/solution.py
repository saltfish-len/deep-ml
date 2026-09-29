def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
	m,n = len(matrix),len(matrix[0])

	if mode == 'row':
		means = [0]*m
		for i in range(m):
			for j in range(n):
				means[i] += matrix[i][j]/n


	if mode == 'column':
		means = [0]*n
		for i in range(m):
			for j in range(n):
				means[j] += matrix[i][j]/m
			
	return means