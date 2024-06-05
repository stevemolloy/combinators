def I(x):
    return x

def K(x):
    return lambda y: x

def W(f):
    return lambda x: f(x, x)

def C(f):
    return lambda x, y: f(y, x)

def B(f, g):
    return lambda x: f(g(x))

def B1(f, g):
    return lambda x, y: f(g(x, y))

def S(f, g):
    return lambda x: f(x, g(x))

def D(f, g):
    return lambda x, y: f(x, g(y))

def psi(f, g):
    return lambda x, y: f(g(x), g(y))

# Examples
square = lambda x: x**2
plus = lambda x, y: x + y
sqr_root = lambda x: x**0.5

hypot = B1(sqr_root, psi(plus, square))

