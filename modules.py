import matematik

print(matematik.topla(10,20))

print("**************")

#alias
import matematik as deneme
#built-in modules
import random
#package

print(deneme.topla(10,20))

print(random.randint(0,100))

print("**************")

from matematik import topla as toplamaIslemi
from day2 import sayHello

print(toplamaIslemi(10,20))

print(random.randint(0, 100))