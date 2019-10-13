# program to print a matrix
def matrix1(mat):
  for row in range(0,3):
    print(arr[row]) # print internal element of mat list 

def matrix2(mat):
  for row in range(0,3):
    for col in range(0,3):
      print(row,col) 
      
#driver code
# A 3X3 matrix as a 2d list in python
mat = [[1,2,3],[4,5,6],[7,8,9]]
#calling method
matrix1(mat)
matrix2(mat)
