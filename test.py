def ami():
    x = []
    z = []
    for i in range(10):
        x.append(i)
    for j in range(5):
        z.append(j)
    return x, z
y = ami()
print(y[0])