from collections import Counter
import math

train = """the student is intelligent
the student studies python
the teacher teaches python
python is easy to learn"""

test = """the student studies python"""

w = train.lower().split()
test = test.lower().split()

u = Counter(w)
b = Counter(zip(w,w[1:]))
t = Counter(zip(w,w[1:],w[2:]))

def H(p):
    p = [x for x in p if x > 0]
    return -sum(math.log2(x) for x in p)/len(p)

p1 = [u[x]/len(w) for x in test]

p2 = [b[x,y]/u[x] if u[x] else 0
      for x,y in zip(test,test[1:])]

p3 = [t[x,y,z]/b[x,y] if b[x,y] else 0
      for x,y,z in zip(test,test[1:],test[2:])]

print("Unigram Entropy:",round(H(p1),3))
print("Bigram Entropy:",round(H(p2),3))
print("Trigram Entropy:",round(H(p3),3))
