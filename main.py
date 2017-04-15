import math
import copy # for deep copy

class Matrix(object):

	def __init__(self,A,order):
		self.A = copy.deepcopy(A)
		self.order = order


	def __str__(self):
		returned_string = ''

		for i in range(1,self.order+1):
			for j in range(1,self.order+1):
				returned_string += str(self.A[i][j]) + " "
			returned_string += "\n"

		return returned_string.strip()


	def transpose(self):
		inverted = copy.deepcopy(self.A)
		for i in range(1,order+1):
			for j in range(1,order+1):
				inverted[j][i] = self.A[i][j]

		return Matrix(inverted,self.order)

	def multiply(self,other):
		multi = copy.deepcopy(self.A)

		for i in range(1,self.order+1):
			for j in range(1,self.order+1):
				for k in range(1,self.order+1):
					multi[i][j] += self.A[i][k]*other.A[k][j]
				multi[i][j] = multi[i][j]-self.A[i][j]
		return Matrix(multi,self.order)


class twoBytwo(Matrix):

	def determinant(self):
		B = self.A
		ans = (B[1][1] * B[2][2]) - (B[2][1] * B[1][2])
		return ans

	def inverse(self):
		det = self.determinant()
		adj = copy.deepcopy(self.A)
		adj[1][1] = self.A[2][2]/float(det)
		adj[2][2] = self.A[1][1]/float(det)
		adj[1][2] = -adj[1][2]/float(det)
		adj[2][1] = -adj[2][1]/float(det)
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

	def inverse(self):
		B = self.A
		minors = copy.deepcopy(self.A)

		for x in range(1,4):
			for y in range(1,4)
				z = []

				for i in range(1,4):
					for j in range(1,4):
						if (x==i) or (y==j) :
							pass
						else:
							z.append(B[i][j])
				Z = [None,[None,z[0], z[1]], [None,z[2], z[3]]]
				twoBytwoSub = twoBytwo(copy.deepcopy(Z),2)
				subDeterminant = twoBytwoSub.determinant()
				if y%2==0:
					ans = -1 * subDeterminant
				else:
					ans = subDeterminant



order = 3

if order == 2:
	a11 = 1
	a12 = 2
	a21 = 3
	a22 = 4
	A = [None,[None,a11, a12], [None,a21, a22]]
	our_matrix = twoBytwo(copy.deepcopy(A),order)
	x = our_matrix.inverse()
	print x

if order == 3:
	a11 = 1
	a12 = 2
	a13 = 3
	a21 = 4
	a22 = 5
	a23 = 6
	a31 = 7
	a32 = 8
	a33 = 9
	A = [None,[None,a11, a12, a13], [None,a21, a22, a23], [None,a31, a32, a33]]
	matrixA = threeBythree(copy.deepcopy(A),order)
	x = matrixA.determinant()
	print x















