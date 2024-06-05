# My attempt att summarising what I have learnt from:
#    - https://raw.githubusercontent.com/codereport/Content/main/Publications/Combinatory_Logic_and_Combinators_in_Array_Languages.pdf

def I(x):
    return x

def K(x):
    return lambda y: x

def W(f):
    return lambda x:    f(x, x)

def C(f):
    return lambda x, y: f(y, x)

def B(f, g):
    return lambda x:    f(g(x))

def B1(f, g):
    return lambda x, y: f(g(x, y))

def S(f, g):
    return lambda x:    f(x, g(x))

def D(f, g):
    return lambda x, y: f(x, g(y))

def D2(f, g, h):
    return lambda x, y: f(g(x), h(y))

def psi(f, g):
    return lambda x, y: f(g(x), g(y))

def phi(f, g, h):
    return lambda x:    f(g(x), h(x))

def phi1(f, g, h):
    return lambda x, y: f(g(x, y), h(x, y))

# Examples
KI = K(I)

square =   lambda x:    x**2
plus =     lambda x, y: x + y
minus =    lambda x, y: x - y
sqr_root = lambda x:    x**0.5

hypot = B1(sqr_root, psi(plus, square)) # BQN: Hypot ← √∘(+○(×˜))
span = phi(minus, max, min)             # BQN: Span ← (⌈´-⌊´)
