def countwords(str):
	d = {}
	split_str = str.split(' ')

	for i in split_str:
		d[i] = split_str.count(i)

	return d