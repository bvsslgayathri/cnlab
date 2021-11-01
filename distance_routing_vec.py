INF=999
'''
adj=[]
v=int(input("enter no.of vertices "))
adj=[[0 if(i==j) else INF for j in range(v)]for i in range(v)]
e=int(input("enter no.of edges "))
for k in range(e):
    v1,v2=int(input("enter the vertices ")),int(input())
    adj[v1][v2]=int(input("enter the weight of the edges "))
    adj[v2][v1]=adj[v1][v2]
'''
v=int(input())
adj=[list(map(int,input().split())) for i in range(v)]

'''
0 5 2 3 999
5 0 4 999 3
2 4 0 999 4
3 999 999 0 999
999 3 4 999 0

'''
# v=5
# adj=[[0, 5, 2, 3, 999], [5, 0, 4, 999, 3], [2, 4, 0, 999, 4], [3, 999, 999, 0, 999], [999, 3, 4, 999, 0]]
print(adj)
dv=[]
for i in range(v):
    temp=[]
    for j in range(v):
        temp.append(i)
    dv.append(temp)

print(dv)


for k in range(v):
    for i in range(v):
        for j in range(v):
            if(adj[i][k]+adj[k][j]<adj[i][j]):
                adj[i][j]=adj[i][k]+adj[k][j]
                dv[i][j]=k
                
            else:
                adj[i][j]=adj[i][j]
            
i,j=int(input()),int(input())
print("Distance between router ",i," and router ",j," is " ,adj[i][j],"via",dv[i][j])

# for i in range(v):
#     for j in range(v):
#         if x==i and y==j:            
#             print("Distance between router ",i," and router ",j," is " ,adj[i][j],"via",dv[i][j])
