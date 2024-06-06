# My attempt at summarising what I have learnt from:
#    - https://raw.githubusercontent.com/codereport/Content/main/Publications/Combinatory_Logic_and_Combinators_in_Array_Languages.pdf

I    = lambda x: x
K    = lambda x: lambda y: x
KI   = K(I)
W    = lambda f: lambda x: f(x)(x)
C    = lambda f: lambda x: lambda y: f(y)(x)
B    = lambda f: lambda g: lambda x: f(g(x))
B1   = lambda f: lambda g: lambda x: lambda y: f(g(x)(y))
S    = lambda f: lambda g: lambda x: f(x)(g(x))
D    = lambda f: lambda g: lambda x: lambda y: f(x)(g(y))
D2   = lambda f: lambda g: lambda h: lambda x: lambda y: f(g(x))(h(y))
psi  = lambda f: lambda g: lambda x: lambda y: f(g(x))(g(y))
phi  = lambda f: lambda g: lambda h: lambda x: f(g(x))(h(x))
phi1 = lambda f: lambda g: lambda h: lambda x: lambda y: f(g(x)(y))(h(x)(y))

# Examples

times =    lambda x: lambda y: x*y
plus =     lambda x: lambda y: x + y
minus =    lambda x: lambda y: x - y
sqr_root = lambda x:           x**0.5
equals =   lambda x: lambda y: x == y
reverse =  lambda xs:          xs[::-1]

square = W(times)                       # BQN: Square ← ×˜
hypot = B1(sqr_root)(psi(plus)(square)) # BQN: Hypot ← √∘(+○(×˜))
span = phi(minus)(max)(min)             # BQN: Span ← ⌈´-⌊´
is_palindrome = S(equals)(reverse)      # BQN: Is_palindrome ← ≡⟜⌽

# Bools
T = K
F = KI

NOT = lambda x: x(F)(T)
AND = lambda x: lambda y: x(y)(x)
OR  = lambda x: lambda y: x(x)(y)
XOR = lambda x: lambda y: x(NOT(y))(y)

# Numerals
church2int = lambda n: n(lambda x: x+1)(0) # Converts the Church numeral to Python int

SUCC = lambda n: lambda f: lambda x: f(n(f)(x))
ADD = lambda n1: lambda n2: n1(SUCC)(n2)
MULTIPLY = B

ZERO  = F
ONE   = lambda f: lambda x: f(x)
TWO   = lambda f: lambda x: f(f(x))
THREE = lambda f: lambda x: f(f(f(x)))
FOUR = SUCC(THREE)
FIVE = SUCC(FOUR)
SIX = SUCC(SUCC(SUCC(THREE)))
SEVEN = ADD(THREE)(FOUR)
EIGHT = ADD(SUCC(TWO))(FIVE)
NINE = SUCC(ADD(ONE)(SEVEN))
TEN = ADD(MULTIPLY(TWO)(THREE))(FOUR)
TWENTY_SEVEN = MULTIPLY(THREE)(NINE)

