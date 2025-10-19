#John is trying to solve the arithmetic series(AP). He wants to find two things in the series                  
#1. He wants to find nth terms in the series             
#2. He wants to find the sum up to the nth term.

series = (2, 4, 6, 8, 10)

a=2
n=5 
d=2

# an = a+(n-1)d  (formula fot nth term)
an = (a+(n-1)*d)
print ("nth term in the series is {}".format(an))

# Sn = (n/2)(2a + (n-1)d) = (n/2)(a+an) (formula for sum up to nth series)
Sn = (n/2)*(a+an)
print(f"Sum of the series is {Sn}")