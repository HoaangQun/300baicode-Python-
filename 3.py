xC, yC = map(float, input("Nhap toa do tam C(xC, yC)? ").split())
R = float(input("Nhap ban kinh R? "))
M = input("Nhap toa do M(xM, yM)? ")
xM, yM = map(float, M.split())
d = ((xM - xC)**2 + (yM - yC)**2)**0.5
if d == R:
    print("Diem M nam tren duong tron")
elif d < R:
    print("Diem M nam trong duong tron")
else:
    print("Diem M nam ngoai duong tron")