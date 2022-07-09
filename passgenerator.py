import random
import string

lst = []
e = int(input("password length?"))
n = random.randint(1,e)
for i in range(n):
    #lst.append(random.choice(string.ascii_letters)[0])
    #lst.append(random.choice(string.ascii_letters)[0])
    #lst.append(random.choice(string.printable)[0])
    lst.append(random.choice(string.printable)[0])
    
print("".join(lst))


