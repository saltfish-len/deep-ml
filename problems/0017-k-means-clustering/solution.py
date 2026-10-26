def k_means_clustering(points: list[tuple[float, ...]], k: int, initial_centroids: list[tuple[float, ...]], max_iterations: int) -> list[tuple[float, ...]]:
	# Your code here
	import numpy as np
	points = np.array(points, dtype=float)
	centroids = np.array(initial_centroids, dtype=float)
	for i in range(max_iterations):
		# distence
		dist = np.linalg.norm(points[:,None,:]-centroids[None,:,:],axis=-1) # n, k
		# assign
		assign = np.argmin(dist, axis=1) # n
		# move
		for cid in range(k):
			centroids[cid,:] = points[assign==cid].mean(axis = 0)
	final_centroids = [tuple(np.round(c, 4)) for c in centroids]
	return final_centroids