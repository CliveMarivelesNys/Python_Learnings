import numpy as np

a = np.array([55, 60, 65, 70, 75, 80])
b = np.array([20, 25, 30, 35, 40, 45])
c = 0
d = 1
sum = 0

print("Original Scores: ", a)
print("Original Ages: ", b)

for x in np.nditer(a,op_flags=['readwrite']):
    if (c < 3):
        x[...] = 5 + x
        c = c + 1

    else:
        x[...] = x

print("Updated Scores: ", a)

for x in np.nditer(b, op_flags=['readwrite']):
    if (d < 4):
        x[...] = 1 + x
        d = d + 1

    else:
        x[...] = x

print("Updated Ages: ", b)
zipped = list(zip(a,b))
print("Ages Score pairs: ", zipped)
print("Unzipped Scores", a)
print("Unzipped Ages", b)

for l in range(0, len(a)):
    sum = sum + a[l];

print("Sum of all scores" + str(sum))

def interface_arrayediter():
    print("w")