from flask import Flask

app = Flask(__name__)

@app.route("/say_hi", methods=["GET"])
def hi():
	data = request.json
	return f"reply from endpoint hi, data = {data}"

@app.route("/say_bye", methods=["GET"])
def bye():
	return f"reply from endpoint bye"

if __name__ == "__main__":
	app.run(debug=True)