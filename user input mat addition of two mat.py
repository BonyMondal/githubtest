r=int(input("enter the number of row: "))
c=int(input("enter the number of columns: "))
matrix=[]
l=[]
print("enter the entries row wise: ")
for i in range(r):
    a=[]
    for j in range(c):
        a.append(input())
    matrix.append(a)
for i in range(r):
    for j in range(c):
        print(matrix[i][j],end=" ")
    print( )
r2=int(input("enter the number of row: "))
c2=int(input("enter the number of columns: "))
matrix2=[]
l2=[]
print("enter the entries row wise: ")
for i in range(r2):
    a1=[]
    for j in range(c2):
        a1.append(input())
    matrix2.append(a1)
for i in range(r2):
    for j in range(c2):
        print(matrix2[i][j],end=" ")
    print( )
result=[[0,0,0],[0,0,0],[0,0,0]]
for i in range(r):
    for j in range(c):
                   result[i][j]=matrix[i][j] + matrix2[i][j]
   # print("resultant matrix is: ")
    for r in result:
        print(result)
