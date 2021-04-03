

def solution(answers):
    student1=[1,2,3,4,5]
    student2=[2,1,2,3,2,4,2,5]
    student3=[3,3,1,1,2,2,4,4,5,5]
    cnt1=0
    cnt2=0
    cnt3=0
    answer = []

    for i in range(len(answers)):
        if(answers[i]==student1[i%len(student1)]):
            cnt1+=1
        if (answers[i] == student2[i % len(student2)]):
            cnt2 += 1
        if (answers[i] == student3[i % len(student3)]):
            cnt3 += 1
    m=max(cnt1,cnt2,cnt3)

    if (m == cnt1): answer.append(1)
    if (m == cnt2): answer.append(2)
    if (m == cnt3): answer.append(3)
    return answer