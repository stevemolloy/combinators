# My attempt att summarising what I have learnt from:
#    - https://raw.githubusercontent.com/codereport/Content/main/Publications/Combinatory_Logic_and_Combinators_in_Array_Languages.pdf

def I(x):
    return x

def K(x):
    return lambda y: x

def W(f):
    return lambda x: f(x)(x)

def C(f):
    return lambda x: lambda y: f(y)(x)

def B(f, g):
    return lambda x: f(g(x))

def B1(f, g):
    return lambda x: lambda y: f(g(x)(y))

def S(f, g):
    return lambda x: f(x)(g(x))

def D(f, g):
    return lambda x: lambda y: f(x)(g(y))

def D2(f, g, h):
    return lambda x: lambda y: f(g(x))(h(y))

def psi(f, g):
    return lambda x: lambda y: f(g(x))(g(y))

def phi(f, g, h):
    return lambda x: f(g(x))(h(x))

def phi1(f, g, h):
    return lambda x: lambda y: f(g(x)(y))(h(x)(y))

# Examples
KI = K(I)

times =    lambda x: lambda y: x*y
plus =     lambda x: lambda y: x + y
minus =    lambda x: lambda y: x - y
sqr_root = lambda x:           x**0.5
equals =   lambda x: lambda y: x == y
reverse =  lambda xs:          xs[::-1]

square = W(times)                       # BQN: Square ← ×˜
hypot = B1(sqr_root, psi(plus, square)) # BQN: Hypot ← √∘(+○(×˜))
span = phi(minus, max, min)             # BQN: Span ← ⌈´-⌊´
is_palindrome = S(equals, reverse)      # BQN: Is_palindrome ← ≡⟜⌽

# Bools
T = K
F = KI

NOT = lambda x: x(F)(T)
AND = lambda x: lambda y: x(y)(x)
OR  = lambda x: lambda y: x(x)(y)

