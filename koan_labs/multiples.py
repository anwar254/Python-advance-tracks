def multiple_sum():
	
	thao = range(1, 1000)
	lst = []
	for i in thao:
		if i % 3 == 0 or i % 5 == 0:
			lst.append(i)

	return sum(i for i in lst)
	