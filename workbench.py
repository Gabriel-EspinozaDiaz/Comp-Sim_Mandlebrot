from matplotlib import pyplot as plt

x = complex(0.2,0.8)
y = complex(0.13810009,0.6)
z = complex(0,0)

def find_limit(c):
    z = 0
    for n in range(255):
        z = z**2 + c
        if abs(z) > 2:
            return n
    return 255

print(find_limit(x))
print(find_limit(y))
print(find_limit(z))
help(plt.imshow)







"""print(spadoof)
print(spadoof.conjugate())
print(spadoof.real)
print(spadoof.imag)
print(cmath.phase(spadoof))
print(cmath.polar(spadoof))"""
