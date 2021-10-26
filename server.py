import socket            
s = socket.socket()        
print ("Socket successfully created")
port = 34487       
s.bind(('', port))        
print ("socket binded to %s" %(port))
 
s.listen(5)    
print ("socket is listening")           
 

c, addr = s.accept()
print ('Got connection from', addr )
y=''
i=0
while True:
    x=c.recv(1024).decode()
    print("received char",x)
    y='acknowledgement sent '+x
    print(y)
    if i==0:
        y=' '
        i+=1
    c.send(y.encode())
    i+=1
    if y=='acknowledgement sent ;':
        print('yes')
        break
c.close()
