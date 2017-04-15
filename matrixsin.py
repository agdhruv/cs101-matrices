import math
import copy#using this to import deepcopy which will copy lists inside list

class Matrix(object):
	def __init__(self,A,order):
		self.A=copy.deepcopy(A)
		self.order= order


	def __str__(self):
		new_string=''

		for i in range(1,self.order+1):
			for j in range(1,self.order+1):
				new_string=new_string+str(self.A[i][j])+" "
			new_string=new_string+"\n"
		return new_string.strip()

	def transpose(self):
		trans=copy.deepcopy(self.A)
		for i in range(1,self.order+1):
			for j in range(1,self.order+1):
				trans[j][i]=self.A[i][j]
		return Matrix(trans,self.order)


	def multiply(self,other):
		multi = copy.deepcopy(self.A)

		for i in range(1,self.order+1):
			for j in range(1,self.order+1):
				for k in range(1,self.order+1):
					multi[i][j] += self.A[i][k]*other.A[k][j]
				multi[i][j] = multi[i][j]-self.A[i][j]
		return Matrix(multi,self.order)



class twobytwo(Matrix):
	#this class has inherited the class Matrix along with its init function
	def determinant(self):
		B=copy.deepcopy(A)
		det_ans=B[1][1]*B[2][2]-B[1][2]*B[2][1]
		return det_ans
	

	def inverse(self):
		det=self.determinant()
		adj=copy.deepcopy(self.A)
		adj[1][1]=self.A[2][2]/float(det)
		adj[1][2]=-self.A[1][2]/float(det)
		adj[2][1]=-self.A[2][1]/float(det)
		adj[2][2]=self.A[1][1]/float(det)
		return Matrix(adj,2)


class threeBythree(Matrix):

	def determinant(self):
		B = self.A
		ans = 0

		for x in range(1,4):
			z = []

			for i in range(2,4):
				for j in range(1,4):
					if j==x:
						pass
					else:
						z.append(B[i][j])
			Z = [None,[None,z[0], z[1]], [None,z[2], z[3]]]
			twoBytwoSub = twoBytwo(copy.deepcopy(Z),2)
			subDeterminant = twoBytwoSub.determinant()
			if x%2==0:
				ans += -B[1][x] * subDeterminant
			else:
				ans += B[1][x] * subDeterminant
		return ans


order=3

A=[None,[None,1,2,3],[None,4,5,6], [None,7,8,9]]
matrixA = twobytwo(copy.deepcopy(A),order)

m = matrixA.multiply(matrixA)
print m