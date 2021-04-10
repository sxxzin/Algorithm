n=int(input())#정점의 갯수
m=int(input())#간선의 갯수
matrix = [[0]*(n+1) for i in range(n+1)] #n+1 행렬
visit_list=[0]*(n+1)

for i in range(m):
    x,y=map(int, input().split())
    matrix[x][y]=matrix[y][x]=1

def dfs(v1):
    visit_list[v1]=1 #방문한 점 1로 표시
    for i in range(1,n+1):
        if(visit_list[i]==0 and matrix[v1][i]==1):
            dfs(i)


dfs(1)
cnt=-1
for i in visit_list:
    if i==1:
        cnt+=1
print(cnt)