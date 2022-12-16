def share_bread(N, K):
    x = K // N
    y = K % N
    return x, y

# если в функции всё верно, то после выполнения этой строчки, не должно выскакивать ошибок
assert share_bread(N=3, K=14) == (4, 2)