import math
import itertools

def isPrime(n):
    if (n<2):
        return False;

    for i in range(2,int(math.sqrt(n)+1)):
        if (n%i==0):
            return False;
    else:
        return True;



def solution(num):
    from itertools import permutations

    answer = 0
    list_com = list(num)
    for i in range(2,len(num)+1):
        permutations_list = list(permutations(num, i)) #순열로 숫자 조합
        for j in permutations_list:
            list_com.append(''.join(j))
    list_com = list(set([int(x) for x in list_com])) # 중복되는 값 제거
    print(list_com)
    for i in list_com:
        if isPrime(i):
            answer += 1
        else:
            pass

    return answer


numbers="011"
print(solution(numbers))