def xor_prod(num1,num2):
    res=[]
    for i in range(len(num1)):
        res.append(int(num1[i])^int(num2[i]))
    return res

def func(divisor,data):
    res=list(data[0:len(divisor)])
    for i in range(len(res)-1):
        data.pop(0)

    while len(data)>0:
        if int(res[0])==1:
            res=xor_prod(res,divisor)
        res.pop(0)
        data.pop(0)
        if len(data)>0:
            k=data[0]
            res.append(k)
            
    return res

n=input()
k=input()#divisor

n1=n+'0'*(len(k)-1)
# k=k.lstrip('0') 
res=list(n)+func(list(k),list(n1))
s = ''.join(map(str, res))

res1=func(list(k),list(s))
s = ''.join(map(str, res1))

if int(s)==0:
    print("success") 
else:
    print("error")

'''
10110110
1011
'''

'''
1101011011
10011
'''