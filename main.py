
import numpy as np
import cv2
from random import randint
from time import time
from numba import njit

@njit()
def check(s):
    centrale = s[1, 1]
    sum = np.sum(s)-centrale
    if centrale == 1:
        if sum == 2 or sum == 3:
            return 1
        else:
            return 0
    else:
        if sum == 3:
            return 1
        else:
            return 0

@njit()
def aggiorna(m):
    x, y = m.shape
    mNew = np.zeros((x, y))
    for i in range(1, x-1, 1):
        for j in range(1, y-1, 1):
            mNew[i, j] = check(m[i-1:i+2, j-1:j+2])
    return mNew

m = np.zeros((100, 100), np.bool)
out = np.zeros((100, 100, 3))
#m[40:50, 40:50] = 1
print(m)

while True:
    t0 = time()
    rx, ry = randint(0, 100), randint(0, 100)
    m[rx-1:rx+2, ry-1:ry+2] = 1
    m = aggiorna(m)
    out[:, :, 1] = m
    img = cv2.resize(out, (1000, 1000), interpolation=cv2.INTER_NEAREST)
    cv2.imshow("W1", img)
    k = cv2.waitKey(2)
    if k == 27:
        break
    print(1/(time()-t0))

cv2.destroyAllWindows()
