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


order = 2

if order == 2:
	a11 = 1
	a12 = 2
	a21 = 3
	a22 = 4
	A = [None,[None,a11, a12], [None,a21, a22]]
	our_matrix = twoBytwo(copy.deepcopy(A),order)
	x = our_matrix.inverse()
	print x















