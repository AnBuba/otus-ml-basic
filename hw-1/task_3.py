def amulet_area(a, b, c):
    p = (a + b + c) / 2
    S = (p * (p - a) * (p - b) * (p - c))**(1 / 2)
    return S

assert amulet_area(3, 4, 5) == 6