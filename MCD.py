# programa q halla el MCD


def MCD(x,y):
 

   if x>y:
      r=x%y
   
      while r>0:
	   b=r
	   r=y%r
   	   y=b
      if r==0:
         pass
      return y

   else:
      r=y%x
   
      while r>0:
	   b=r
	   r=x%r
	   x=b
      if r==0:
	 pass
      return x

print "ingresa dos numeros a los cuales quieras hallarles el MCD"
x=raw_input()
y=raw_input()
print "ingresa el MCD que crees que tienen"
z=raw_input()
l=MCD(int(x),int(y))
if l==int(z):
   print ("bien hecho "+ z + " es el MCD de "+ x + " y " +y )
else:
   print ("intenta otra vez")
	   
