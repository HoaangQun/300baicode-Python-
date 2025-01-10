import random
mp = 0
pcp = 0
while True:
        print ("-- keo bua bao ( nhấn bất kì phím nào để thoát ):")
        me = input (">> ")
        if me == 'keo' or me == 'bua' or me == 'bao':
                print ("you: ",me)
                pc_ = random.randint (1,3)
                if pc_ == 1:
                        pc = 'keo'
                elif pc_ == 2:
                        pc = 'bua'
                else:
                        pc = 'bao'

                print ("bot: ",pc)
                a = '> thang'
                b = '> thua'
                c = '> hoa'
                if me == pc:
                        kq = c
                else:
                        if pc == 'keo' and me == 'bua':
                                kq = a
                        elif pc == 'bua' and me == 'bao':
                                kq = a
                        elif pc == 'bao' and me == 'keo':
                                kq = a
                        else:
                                kq = b
                print (kq)
                if kq == a:
                        mp += 1
                elif kq == b:
                        pcp += 1
                print (mp, "-",pcp)
        else:
                break

print ("Thoát thành công!!")