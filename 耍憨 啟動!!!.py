import random
N = random.randrange(101)
n = None
while n!=N:
    n = int(input("猜:"))
    if n>N:
        print("<")
    elif n<N:
        print(">")

print("gg")