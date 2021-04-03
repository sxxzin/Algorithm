from collections import Counter

list1=[]
list2=[]
result=[]
n=input()
list1=list(map(int, input().split()))
m=input()
list2=list(map(int, input().split()))

list1 = Counter(list1)

for i in list2:
    result.append(list1[i])

for i in result:
    print(i, end = ' ')