def dien_tich_tam_giac(x1, y1, x2, y2, x3, y3):
    return abs((x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2)
xA, yA = map(float, input("Nhập vào toạ đô điểm A: ").split())
xB, yB = map(float, input("Nhập vào toạ đô điểm B: ").split())
xC, yC = map(float, input("Nhập vào toạ đô điểm C: ").split())
xM, yM = map(float, input("Nhập vào toạ đô điểm M cần kiểm tra: ").split())
sABC = dien_tich_tam_giac(xA, yA, xB, yB, xC, yC)
sMAB = dien_tich_tam_giac(xM, yM, xA, yA, xB, yB)
sMBC = dien_tich_tam_giac(xM, yM, xB, yB, xC, yC)
sMCA = dien_tich_tam_giac(xM, yM, xC, yC, xA, yA)
total_sM = sMAB + sMBC + sMCA
if total_sM == sABC:
    print(">> M nằm trong hoặc trên tam giác ABC")
elif sMAB == 0 or sMBC == 0 or sMCA == 0:
    print(">> M nằm trên một đoạn thẳng bất kì của tam giác ABC")
else:
    print(">> M nằm ngoài tam giác ABC")        

