l=int(input())#문자열 길이
str=input()#문자열
sum=0

for i in range(len(str)):
    sum+=(ord(str[i])-96)*(31**i)

print(sum%1234567891)