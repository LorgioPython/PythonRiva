

#Fibonacci

def Fibonacci (n):  		#Donde n es un natural
	if n ==0: return [1]
	else:
		salida=[1]
		a,b = 0,1				#Asignación múltiple      
		for x in range(n):  	#Creo una secuencia 1,2,...,n con range
			salida.append(b) 
			a, b = b, a+b
			
		return salida







