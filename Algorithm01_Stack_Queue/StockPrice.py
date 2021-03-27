#deque로 구현
from collections import deque

prices = [1,2,3,2,3]

def solution(prices):
    answer = []
    prices=deque(prices)
    while prices:
        temp=prices.popleft()
        cnt=0
        for i in prices:
            if temp>i:
                cnt += 1
                break
            cnt +=1
        answer.append(cnt)
    return answer

print(solution(prices))

#list로 구현

def solution(prices):
    answer = [0] * len(prices)
    for i in range(len(prices)):
        for j in range(i+1, len(prices)):
            answer[i] += 1
            if prices[j] < prices[i]:
                break

    return answer