def primos (n):
    
    for j in range(2,n):
	
        for x in range(2,j):
		
            if j % x == 0:
                
                break     
        else :
			print j
