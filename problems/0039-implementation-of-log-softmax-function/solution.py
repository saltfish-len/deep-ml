import numpy as np

def log_softmax(scores: list) -> np.ndarray:
	# Your code here
	# log(exp(i)/sum(exp(x)))
	# log(exp(i))-log(sum(exp(x)))
	# safe:
	# i-m - log(sum(exp(x-m)))
	scores = np.array(scores)
	m = np.max(scores)
	scores -= m 
	nomi = np.log(np.sum(np.exp(scores)))
	return scores-nomi