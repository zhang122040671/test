for i in range(1,10):
    for j in range(1,i+1):
        print("%d×%d=%d"%(j,i,j*i),end="\t")
    print("")

count=0
total=0
while count<=100:
     total=total+count
     count=count+1
print("1+2+3+...+100=%d"%total)
