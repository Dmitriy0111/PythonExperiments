# test Complex class
from Complex import Complex

a = Complex(-1.5,2)
print("a value = %f %f" %a.info())
b = Complex(4,-2.5)
print("b value = %f %f" %b.info())

c = a + b
print("Add result = %f %f" %(c.info()))
d = a - b
print("Sub result = %f %f" %(d.info()))
e = a * b
print("Mul result = %f %f" %(e.info()))
f = a / b
print("Div result = %f %f" %(f.info()))

print( "a!=b" if a != b else "a==b")
print( "a==a" if a == a else "a!=a")
print( "b!=a" if b != a else "b==a")
print( "b==b" if b == b else "b!=b")

print("|a|= %f " %a.abs() )

print("|b|= %f " %b.abs() )
