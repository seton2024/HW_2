
import numpy as np

R=np.matrix("200,245,200,200,245,200;200,200,200,200,200,200;200,245,200,200,245,200;200,200,245,245,200,200")
print(R)
print()
G=np.matrix("150,195,150,150,195,150;150,150,150,150,150,150;150,195,150,150,195,150;150,150,195,195,150,150")
print(G)
print()
B=np.matrix("60,150,60,60,150,60;60,60,60,60,60,60;60,150,60,60,150,60;60,60,150,150,60,60")
print(B)
print()
M=np.matrix("250,250,250,250,250,250;250,250,250,250,250,250;250,250,250,250,250,250;250,250,250,250,250,250")

# color inversion
R_m=M-R
print(R_m)
print()
G_m=M-G
print(G_m)
print()
B_m=M-B
print(B_m)
print()

# brightness -80%
R_b=0.8*R
print(R_b)
print()
G_b=0.8*G
print(G_b)
print()
B_b=0.8*B
print(B_b)
print()

#rotate 90
print(R.T)
print()
print(G.T)
print()
print(B.T)
print()
print(HW)

print("pineapple")
