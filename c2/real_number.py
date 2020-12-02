# pair
def pair(a, b):
    def get(i):
        if i == 0:
            return a
        elif i == 1:
            return b

    return get


def select(p, i):
    return p(i)


# real number
def real_number(a, b):
    from math import gcd
    g = gcd(a, b)
    return pair(a // g, b // g)


def numer(p):
    return select(p, 0)


def denum(p):
    return select(p, 1)


# operate real number
def add_real_number(a, b):
    return real_number(
        numer(a) * denum(b) + denum(a) * numer(b),
        denum(a) * denum(b))


def print_real_number(n):
    print(numer(n), '/', denum(n))


def mul_real_number(a, b):
    return real_number(numer(a) * numer(b), denum(a) * denum(b))


def devide_real_number(a, b):
    return mul_real_number(a, real_number(denum(b), numer(b)))


if __name__ == "__main__":
    n = real_number(2, 3)
    print_real_number(n)
    print_real_number(add_real_number(n, n))
    print_real_number(mul_real_number(n, n))
    print_real_number(devide_real_number(n, n))
