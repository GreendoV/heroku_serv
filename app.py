from flask import Flask,request

app = Flask(__name__)

@app.route('/')
def welcome():
	return "Welcome to my Server for DeezerAPI"

@app.route('/api')
def getCode():
	code = request.args.get('code')
	return code
if __name__ == '__main__':
	app.run(host='0.0.0.0')
