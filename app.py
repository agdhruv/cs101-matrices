from flask import Flask, render_template, request, abort, redirect, url_for
from main import *

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def index():
	if request.method == "GET":
		return render_template("index.html")
	try:
		a11 = int(request.form["a11"])
		a12 = int(request.form["a12"])
		a13 = int(request.form["a13"])
		a21 = int(request.form["a21"])
		a22 = int(request.form["a22"])
		a23 = int(request.form["a23"])
		a31 = int(request.form["a31"])
		a32 = int(request.form["a32"])
		a33 = int(request.form["a33"])
		A = [None,[None,a11, a12, a13], [None,a21, a22, a23], [None,a31, a32, a33]]
		matrixA = threeBythree(copy.deepcopy(A),3)
		x = matrixA.determinant()

		return str(x)

	except Exception, e:
		return str(e)

if __name__ == '__main__':
	app.run(debug=True)