

bridge_length=2
weight=10
truck_weights=[7,4,5,6]

def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge_q=[0]*bridge_length

    while bridge_q:
        answer+=1 #시작
        bridge_q.pop(0) #트럭이 지나감
        if truck_weights:
            if sum(bridge_q) + truck_weights[0]<=weight:
                bridge_q.append(truck_weights.pop(0)) #다리에 트럭 올림
            else:
                bridge_q.append(0) #중량 초과면 트럭 안올림
    return answer

print(solution(bridge_length, weight, truck_weights))