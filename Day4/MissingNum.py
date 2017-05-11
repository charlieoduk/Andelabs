def find_missing(list1,list2):
	length1 = len(list1)
	length2 = len(list2)

	if length1 == length2:
		return 0
	elif length1 > length2:
		for x in range(length1):
			if list1[x] not in list2:
				return list1[x]
			
	else:
		for i in range(length2):
			if list2[i] not in list1:
				return list2[i]
			