def sort_array(array):
	min_val = len(array)-1
	b = None
	if not isinstance(array, list):
		raise ValueError("Argument must be list not {0}".format(type(array).__name__))
	for j in range(len(array)):
		mix_val = array[j]
		for i in array[j:min_val+1]:
			if b is None:
				b = i
				continue
			elif b > i:
				_ = b
				b = i

			array[j]=b
			array[j+1] = i
		#array[j]=b
		b=None		

array = [5,6,2,7,8,3,0,87,29,1,24,102,276,-1,763,2514,-7,442,-2]
sort_array(array)
print(array)
