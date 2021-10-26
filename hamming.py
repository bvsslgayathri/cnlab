import random 
import copy
data=list(map(int,input().split()))
n=len(data)
plist=[]

p=0
for p in range(n):
    if(2**p>=p+n+1):
        break 

for i in range(p):
    arr=[]
    for j in range(2**i,n+p+1,2**(i+1)):
        for k in range(j,j+2**i):
            if k>n+p:
                break
            arr.append(k)
    plist.append(arr) 

for i in range(p):
    data.insert(2**i-1,0)

p_cpy = copy.deepcopy(plist)

for i in range(p):
    for j in range(len(plist[i])):
        plist[i][j] = data[plist[i][j]-1]
    if sum(plist[i])%2==0:
        data[2**i-1]=0
    else:
        data[2**i-1]=1
     
print("hamming code generated is ")
for i in data:
    print(i,end="")
print()

rand=random.randint(0,n+p-1)
data[rand]=0

#Detection.......
pos=""
for i in range(p):
    for j in range(len(p_cpy[i])):
        p_cpy[i][j] = data[p_cpy[i][j]-1]
    
    if sum(p_cpy[i])%2==0:
        pos='0'+pos
    else:
        pos='1'+pos

if '1' in pos:
    print(" binary position to be corrected is ",pos) 
else:
    print("success")
