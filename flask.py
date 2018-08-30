# route tells you which page you want to request
# slash default page of the website
from flask import flask, render_template
 app = Flask(__name__)

 @app = route("/") #gives u the default page
 def index():
 	return "Hello World"

 @app.route("/<string:name>")
 def hello(name):
 	name = name.capitalize() #now the name returns the name in capital formart.
 	#example, Hello, Brian
 	return f"Hello, {name}!"

 	-----

@app.route("/")
def index():
	return render_template("index.html")
	#Question- How does flask know where to look for the index.html file?
	#flask is immediately going to look inside a sub directory called templates
-------------------------------------------------------
from flask import flask, render_template
app = Flask(__name__)

@app = route("/")
def index():
	return "Hello World"

@app.route("/<string:name>")
def hello(name):
	name = name.capitalize()
	