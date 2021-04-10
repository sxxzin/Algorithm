numbers=[1,1,1,1,1]
target=3

def solution(numbers, target):
    length=len(numbers)
    answer = 0
    def dfs(idx, sum):
        if idx==length:
            if sum== target:
                nonlocal answer
                answer+=1
            return
        else:
            dfs(idx+1,sum+numbers[idx])
            dfs(idx+1,sum-numbers[idx])
    dfs(0,0)
    return answer

print(solution(numbers,target))