import numpy as np

h, w = list(map(int, input().split()))

a = np.array([list(map(int, input().split())) for _ in range(h)], dtype = int)
1
ow = np.ones((w, w), dtype = int)
oh = np.ones((h, h), dtype = int)

yoko = np.dot(a, ow)
tate = np.dot(oh, a)

ans = yoko + tate - a

print(*ans, sep = "\n")
