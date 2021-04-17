n=6
arr1=[46, 33, 33 ,22, 31, 50]
arr2=[27 ,56, 19, 14, 14, 10]


def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        arr1[i]=bin(arr1[i])
        arr2[i]=bin(arr2[i])
        answer.append(int(arr1[i],2)|int(arr2[i],2))

    for i in range(n):
        answer[i]=bin(answer[i])
        answer[i] = answer[i].replace("0b","")
        answer[i] = '0'*(n-len(answer[i]))+answer[i]
        answer[i]=answer[i].replace("1","#")
        answer[i] = answer[i].replace("0"," ")

    return answer

print(solution(n,arr1,arr2))