# cook your dish here
def pathfinder(A):
    n = len(A)
    B = A[1:]
    Root = A[0]
    output = []
    counter = 0
    for i in B:
        if counter==1:
            output.append(Root)
        
        if i[1] != 0:
            output.append(i[1])
        output.append(i[0])
        if i[2] != 0:
            output.append(i[2])
        counter+=1
        
    print(output)
    
   
pathfinder([1,[2,4,5],[3,0,6]])  

#pathfinder([1,[2,4,0],[3,0,5]])
        
        
     