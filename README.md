# cs101-matrices

This is a calculator for operations on 2x2 and 3x3 matrices. It calculates the **determinant**, **transpose** and **inverse** of these matrices, and displays them on the relevant webpage.

This calculator has been developed by [Dhruv Sinha](https://github.com/dhruvsinha) and [Dhruv Agarwal](https://github.com/agdhruv) as a `Flask` webapp as part of our CS101 end-term project under the MIT License.


## Technologies Used

* Python (version 2.7)
* Flask (web development framework built on Python)
* HTML, CSS, JavaScript (jQuery)
* AJAX for asynchronous communication with the server


## How to Run

This project uses a `virtual environment` to make it easier to be replicated to new environments.

The following commands (in this order) need to be executed to make this run:

1. Run `git clone https://github.com/agdhruv/cs101-matrices.git`.
2. Create a virtual environment using `virtualenv <name of environment>` with **python 2.7**.
3. Run `pip install -r requirements.txt` to install all required packages.
4. Run the virtual environment using `source <name of environment>/bin/activate`.
5. Run `python app.py`.