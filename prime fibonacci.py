import itertools
n1,n2 =map(int,input().split( ))
l=[]
k=[]
m=[]
for num in range(n1,n2 + 1):

   if num > 1:
       for i in range(2,num):
           if (num % i) == 0:
               break
       else:
           
           l.append(num)
print(*l)


for j in range(0, len(l)+1):

    for subset in itertools.combinations(l, j):
        k.append(subset)
print(*k)

for num1 in range(len(k)):
    if(num1>1):
        for i in range(2,num1):
            if(num1%i==0):
                break
        else:
            m.append(num1)
print(*m)

m.sort()
#greater no
print(m[-1])
#smallest no
print(*m[:1])

#fibbonacci
low=int(*m[:1])
high=m[-1]
#print(low)
#print(high)
#high=print(m[-1])
"""
print("lower value",low)
print("higher value",high)
"""
for i in range(high):
    sum=high+low
   # low=high
    #high=sum
print(sum)