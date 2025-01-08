#password generator

import random

alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
num = ['1','2','3','4','5','6','7','8','9','0']
symbol = ['!','@','#','$','%','^','&','*','(',')','_']

strong_password = random.choice(alpha) + random.choice(num) + random.choice(symbol)
for i in range(10):
    strong_password += random.choice(alpha + num + symbol)
print("A strong password is: ", strong_password)