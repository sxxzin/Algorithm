import math

n,b = input().split()
sum=0
n=n[::-1]
for i in range(len(n)):
    if(n[i]>='A' and n[i]<='Z'):
        number=ord(n[i])-55
    else:
        number=int(n[i])
    sum += math.pow(int(b), i) * number

print(int(sum))
