# import math

# n=int(input())

# for i in range(n):
#     x=int(input())
#     root=math.sqrt(x)
# print("{:.4f}".format(root))
 
import qrcode
img =qrcode.make("https://github.com/")
img.save("Qrcode github.png")

