# import the Flask class from the flask module
from flask import Flask, render_template
from flask import redirect, url_for, request

# create the application object
app = Flask(__name__)

# use decorators to link the function to a url
@app.route('/')
def home():
    return render_template('Index.html')#return 'hello'   # return a string

@app.route('/sample')
def page3():
    return render_template('page3.html')  # render a template

@app.route('/welcome')
def welcome():
    return render_template('welcome.html')  # render a template

@app.route('/login', methods=['GET', 'POST'])
def login():
	error = None
	if request.method == 'POST':
		if request.form['username'] != 'admin' or request.form['password'] != 'admin':
			error = 'Invalid Credentials. Please try again.'
		else:
			return redirect(url_for('welcome'))
    	return render_template('login.html',error=error)

# start the server with the 'run()' method
if __name__ == '__main__':
    app.run(debug=True)