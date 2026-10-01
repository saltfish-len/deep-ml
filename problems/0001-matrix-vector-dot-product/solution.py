def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:
	# Return a list where each element is the dot product of a row of 'a' with 'b'.
	# If the number of columns in 'a' does not match the length of 'b', return -1.
	m,n = len(a),len(a[0])
	h = len(b)
	if n != h:
		return -1

	# res[i] = sum(a[i][k]*b[k])
	def dot_prod(va,vb):
		# vector dot product
		return sum(x*y for x,y in zip(va,vb))
	
	res = [dot_prod(a[i],b) for i in range(m)]
	return res