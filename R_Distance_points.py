import math
X1 , Y1 , X2 , Y2 = map(int,input().split())
X = (X2-X1)**2
Y = (Y2-Y1)**2
x =(X+Y)**(1/2)

print(f"{x:.9f}")