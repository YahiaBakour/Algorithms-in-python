def Merge_Sort(array):
	#split array recursively
	
    if len(array)>1:
        mid = len(array)//2
        left = array[:mid]
        right = array[mid:]

        Merge_Sort(left)
        Merge_Sort(right)
		
        #start to merge em back together
        i,j,k = 0,0,0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                array[k] = left[i]
                i += 1
            else:
                array[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            array[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            array[k] = right[j]
            j += 1
            k += 1

array = [1,5,7,3,7,1,0,19,39,6,19,53,13,8]
Merge_Sort(array)

print(array)
