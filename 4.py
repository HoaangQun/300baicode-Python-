def tam_giac(a, b, c):
    if a+b<c or a+c<b or b+c<a:
        return False
    else:    
        return True

a, b, c = map(float, input("Nhập độ dài 3 cạnh a,b,c: ").split())

if tam_giac(a,b,c):

    a_ = a**2
    b_ = b**2
    c_ = c**2
    if a == b and b == c:
            print(">> Tam giác đều")
    elif a == b or b == a or c == a:
            print(">> Tam giác cân")
    elif a_ + b_ == c_ or a_ + c_ == b_ or b_ + c_ == a_:
            print(">> Tam giác vuông")
    elif a_ + b_ > c_ or a_ + c_ > b_ or b_ + c_ > a_:
            print(">> Tam giác nhọn")
    elif a_ + b_ < c_ or a_ + c_ < b_ or b_ + c_ < a_:
            print(">> Tam giác tù")
    else:
            print(">> Tam giác thường")
    p = (a+b+c)/2
    S = (p*(p-a)*(p-b)*(p-c))**0.5
    print("Diện tích tam giác =",S)
else:
    print("? 3 cạnh vừa nhập không tạo ra tam giác")
