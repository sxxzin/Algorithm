n,m,v=map(int, input().split())
matrix = [[0]*(n+1) for i in range(n+1)] #n+1 행렬
visit_list=[0]*(n+1)

for i in range(m):
    x,y=map(int, input().split())
    matrix[x][y]=matrix[y][x]=1

def dfs(v1):
    visit_list[v1]=1 #방문한 점 1로 표시
    print(v1, end=' ')
    for i in range(1,n+1):
        if(visit_list[i]==0 and matrix[v1][i]==1):
            dfs(i)


def bfs(v1):
    queue=[v1]
    visit_list[v1]=0 #방문한 점 0으로 표시
    while queue:
        v1=queue.pop(0)
        print(v1, end=' ')
        for i in range(1,n+1):
            if (visit_list[i] == 1 and matrix[v1][i] == 1):
                queue.append(i)
                visit_list[i]=0

dfs(v)
print()
bfs(v)


