from collections import deque

progresses = [93, 30, 55]
speeds =[1,30,5]

def solution(progresses, speeds):
    answer = []
    progresses=deque(progresses)
    speeds=deque(speeds)
    while progresses:
        for i in range(len(progresses)):
            progresses[i]+=speeds[i]
        cnt=0
        for i in range(len(progresses)):
            if progresses[i]>=100:
                cnt+=1
            else:
                break
        if cnt:
            answer.append(cnt)
            for i in range(cnt):
                progresses.popleft()
                speeds.popleft()

    return answer

print(solution(progresses,speeds))