import random
number =str(random.randint(0,9))
alphabet = random.choice("QWERTYUIOPASDFGHJKLZXCVBNM")
smallalphabet = random.choice("qwertyuiopasdfghjklzxcvbnm")
specialchar = random.choice("`!£%&*()^&*(~~#/?<|A!£[]@')")
z = random.choice("`!£%&*()^&*(~~#/?<|A!£qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM0123456789")
for i in range(16):
    x = random.choice([number,alphabet,smallalphabet,specialchar])
    z = z+x

print(z,"is your new password")


