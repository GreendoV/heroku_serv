from flask import Flask,request

app = Flask(__name__)

@app.route('/api')
def getCode():
	code = request.args.get('code')
	return code
if __name__ == '__main__':
	app.run(debug=True, port=5000)
