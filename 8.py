s=0
for i in range(3,0,-1):#3,2,1
    for j in range(i-1):
        print(' ',end=' ')
    for k in range(4-i):
        s=s+1
        print(s,end=' ')
       
    print()
        
