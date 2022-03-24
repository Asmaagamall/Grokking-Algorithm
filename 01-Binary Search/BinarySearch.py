def BinarySearch(List ,low , high, Item):
    
	mid = (low + high) // 2
	guess = List[mid]
	
	while low <= high:
		 if guess < Item:
		 	return BinarySearch(List , mid+1 , high , Item)
		 	
		 elif guess > Item:
		 	return BinarySearch(List , low , mid-1 , Item)
		 	
		 else:
		 	 return mid
		 	 
	return -1
	
print(BinarySearch([1,2,3,4] , 0 , 3 , 5))