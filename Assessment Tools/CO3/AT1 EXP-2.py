from collections import Counter

text = """the student is intelligent
the student is hardworking
the student studies python
the teacher is intelligent
the teacher teaches python
python is easy to learn"""

w = text.lower().split()

u = Counter(w)
b = Counter(zip(w,w[1:]))
t = Counter(zip(w,w[1:],w[2:]))

def U(x):
    return u[x]/len(w)

def B(x,y):
    return b[x,y]/u[x] if u[x] else 0

def T(x,y,z):
    return t[x,y,z]/b[x,y] if b[x,y] else 0

def backoff(x,y,z):
    return T(x,y,z) or B(y,z) or U(z)

def interpolation(x,y,z):
    return .2*U(z)+.3*B(y,z)+.5*T(x,y,z)

q = input("Enter sentence: ").lower().split()
x,y = q[-2],q[-1]

for name,fun in [("Unsmoothed",T),
                 ("Backoff",backoff),
                 ("Interpolation",interpolation)]:

    p = [(z,fun(x,y,z)) for z in u]
    p.sort(key=lambda a:a[1],reverse=True)

    print("\n",name)
    for z,prob in p[:5]:
        print(z,round(prob,3))
