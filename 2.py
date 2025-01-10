xA, yA = map(float, input("(xA yA): ").split())
xB, yB = map(float, input("(xB yB): ").split())

AB = ((xB - xA)**2 + (yB - yA)**2)**(1/2)
print("|AB| =",abs(AB))