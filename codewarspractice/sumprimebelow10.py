sum=0
for i in range(1,10,+1):
    count=0
    for j in range(1, i+1,+1):
        if i%j==0:
          count+=1
    if count==2:
        sum+= j
print(sum)