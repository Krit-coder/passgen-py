import pyperclip
import string
import random
length = int(input("Enter the length of the password(min 7): "))
l=[]
if(length>=7):
    sc = "@_$#"
    a=random.choice(string.ascii_uppercase)
    b=random.choice(string.ascii_lowercase)
    c=random.choice(string.digits)
    d=random.choice(sc)
    result = ''.join((random.choice(string.ascii_letters + string.digits + sc) for x in range(length-4)))
    l.append(a)
    l.append(b)
    l.append(c)
    l.append(d)
    for k in result:
        l.append(k)

    random.shuffle(l)
    password=""
    for h in l:
        password+=str(h)
    print("Your Password: ",password)
    pyperclip.copy(password)
else:
    print("Minimum length is 7...\nTry again later")