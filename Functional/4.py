def recur_fibo(n):
   if n <= 1:
       return n
   else:
       return(recur_fibo(n-1) + recur_fibo(n-2))

nterms = int(input("Enter number: "))
s=0
if nterms <= 0:
   print("Plese enter a positive integer")
else:
   for i in range(nterms):
        s=recur_fibo(i)

print(s)