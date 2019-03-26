import string
import random

a=''.join(random.choice(string.ascii_uppercase+string.ascii_lowercase) for k in range(10))
print(a)
for i in string.ascii_uppercase+string.ascii_lowercase:
    b=a.count(i)
    print(i,b)

