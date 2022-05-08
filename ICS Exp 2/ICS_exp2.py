# n= alice prime number
n=11
# g= bob prime number
g=7
print("public keys are:",n," and ",g)
# x=random number to generate private key
x=3
# generate private key of alice calculate a using 
# a=(g**x)%n
a=(g**x)%n
print("private key generated of alice is :",a)

# alice sends a to bob

# y=bob random number
y=6

#private key  calculate of bob  using 
# b=(g**y)%n
b=(g**y)%n
print("private key generated of bob is:",b)

# exchange of generated keys 

# bob sends b to alice
# alice compute secret key k1 as
# k1=(b**x)%n
k1=(b**x)%n
print("Symmetric key of Alice:",k1)

# bob computes k2 as 
# k2=(a**y)%n
k2=(a**y)%n
print("Symmetric key of bob:",k2)