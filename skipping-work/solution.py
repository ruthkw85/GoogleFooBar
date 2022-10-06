def solution(x, y):
	# Your code here
	return list(set(x).symmetric_difference(set(y)))[0]
