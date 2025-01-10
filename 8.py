a, b, c = map(float, input("Nhập vào a, b, c: ").split())
print(a,"x^2 +",b,"x +",c,"= 0")
delta = b**2 - 4*a*c
x1 = (-b-(delta**0.5))/2*a
x2 = (-b+(delta**0.5))/2*a
print ("x1 =",x1)
print ("x2 =",x2)