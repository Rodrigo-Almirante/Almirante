# Recursive Solution

def TowerOfHanoi(n , source, destination, auxillary): 
    if n==1: 
        print("Move disk 1 from source",source,"to destination",destination) 
        return
    TowerOfHanoi(n-1, source, auxillary, destination) 
    print("Move disk",n,"from source",source,"to destination",destination) 
    TowerOfHanoi(n-1, auxillary, destination, source) 
          
# Driver code 
n = int(input("Enter an integer:"))
TowerOfHanoi(n,'A','B','C')