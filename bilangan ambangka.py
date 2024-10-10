def solve(a, b):
    def gcd(x, y):
        if y == 0:
            return x
        else:
            return gcd(y, x % y)
    c = gcd(a, b) #memanggil fungsi gcd dari a dan b, dan menyimpan dlm vrbl c
    d = (a * b) // c #menghitung kpk dn disimpan dalam vrbl d
    result = (c * (d // a)) + (c * (d // b)) #menghitung hasil akhir
    return result
a,b = map(int, input(). split())
print(solve(a, b))