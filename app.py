from flask import Flask, render_template, request, abort, redirect, url_for, jsonify
from main import *

app = Flask(__name__)

@app.route('/')
def index():
	return render_template("index.html")


@app.route('/twoByTwo/')
def twoByTwo():
	return render_template("twoByTwo.html")


@app.route('/threeByThree/')
def threeByThree():
	return render_template("threeByThree.html")


@app.route('/api/twoByTwo', methods=["POST", "GET"])
def api_twoByTwo():
	if request.method == "GET":
		return abort(403)

	try:
		a11 = float(request.form["a11"])
		a12 = float(request.form["a12"])
		a21 = float(request.form["a21"])
		a22 = float(request.form["a22"])
		A = [None,[None,a11, a12], [None,a21, a22]]
		matrixA = twoBytwo(copy.deepcopy(A),2)
		returned_determinant = matrixA.determinant()
		returned_transpose = str(matrixA.transpose())
		if returned_determinant == 0:
			returned_inverse = "Inverse does not exist."
		else:
			returned_inverse = str(matrixA.inverse())
		return jsonify(returned_determinant, returned_transpose, returned_inverse)
	except Exception, e:
		return str(e)


@app.route('/api/threeByThree', methods=["POST", "GET"])
def api_threeByThree():
	if request.method == "GET":
		return abort(403)

	try:
		a11 = float(request.form["a11"])
		a12 = float(request.form["a12"])
		a13 = float(request.form["a13"])
		a21 = float(request.form["a21"])
		a22 = float(request.form["a22"])
		a23 = float(request.form["a23"])
		a31 = float(request.form["a31"])
		a32 = float(request.form["a32"])
		a33 = float(request.form["a33"])
		A = [None,[None,a11, a12, a13], [None,a21, a22, a23], [None,a31, a32, a33]]
		matrixA = threeBythree(copy.deepcopy(A),3)
		returned_determinant = matrixA.determinant()
		returned_transpose = str(matrixA.transpose())
		if returned_determinant == 0:
			returned_inverse = "Inverse does not exist."
		else:
			returned_inverse = str(matrixA.inverse())
		return jsonify(returned_determinant, returned_transpose, returned_inverse)
	except Exception, e:
		return "Error: " + str(e)


if __name__ == '__main__':
	app.run(debug=True)















