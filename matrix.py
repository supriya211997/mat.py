n = (input("enter the number of row"))
m = (input("enter the number of column"))
mat = []
for i in range (0 , 3):
	mat.append([])
for i in range (0 , 3):
	for j in range (0 , 3):
		mat[i].append(j)
		mat[i][j] = 0
for i in range (0 , 3):
	for j in range (0 , 3) :
		print('entry is row: ',i+1,'column:',j+1)
		mat[i][j] = int(input())
print(mat)