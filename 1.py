#tính V dựa vào S
#S = 4.pi.R^2
#V = 4/3.pi.R^2

S = float(input(">>> Nhập vào diện tích S: "))
pi = 3.141593
R = (S/4/pi)**(1/2)
V = R**3 * pi * (4/3)
print(">>> Thể tích V =",V)