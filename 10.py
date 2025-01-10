while True:
    SIN = int(input ("Nhập số sin: (0 để thoát): "))
    if SIN == 0:
        break
    else:
        SIN_ = str (SIN)
        if len (SIN_) != 9:
            print ("Số không hợp lệ!!")
        else:
            check_digit = SIN_ [-1]
            s1 = sum(int(SIN_[i]) for i in range (0, 8, 2))
            s2 = 0
            for i in range (1,8,2):
                s_ = int (SIN_[i])
                if len (str(SIN_[i])) > 1:
                    for k in range (0,2):
                        s_ = str(s_)
                        s_ += int (s_[k])
                s2 += s_ 
            total = s1 + s2 + int (check_digit)
            if total % 10 == 0:
                print("Số SIN hợp lệ!")
            else:
                print ("Số SIN không hợp lệ !")

print ("Thoát thành công")