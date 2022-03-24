def quicksort(List):
    if (len(List) < 2):
        return List
    else:
        pivot = List[0]
        less = [i for i in List[1:] if i <= pivot]
        greatest = [ i for i in List[1:] if i > pivot]
                
        return (quicksort(greteast) + [pivot] + quicksort(less))
    
print(quicksort([2,5,1,7,3,4]))