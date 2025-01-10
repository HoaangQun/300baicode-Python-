import math

x = float (input ("Nhập vào số đo x ( phut ): "))
x_ = x/60
print (x_,"*")
if x_>360:
    x_ = x_%360
if x_ < 0:
    x_ = x_%360+360
if 0<x_<90:
    print ("x thuộc góc phần tư thứ nhất")
if 90<x_<180:
    print ("x thuộc góc phần tư thứ hai")
if 180<x_<270:
    print ("x thuộc góc phần tư thứ ba")
if 270<x_<360:
    print ("x thuộc góc phần tư thứ tư")
radianx = math.radians (x_)
cos_x = math.cos (radianx)
print (cos_x)