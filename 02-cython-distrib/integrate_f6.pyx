cdef double f(double x):
    y = (x*x*x - 3)*x
    return y

def integrate_f6(double a, double b, int n):
    cdef:
        double dx = (b - a) / n
        double dx2 = dx / 2
        double s = f(a) * dx2
        int i = 0
    for i in range(1, n):
        s += f(a + i * dx) * dx
    s += f(b) * dx2
    return s

if __name__ == '__main__':
   print(integrate_f6(-100, 100, 100_000))
