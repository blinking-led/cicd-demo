from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
	return{
		"service":"cicd-demo",
		"version": "1.0",
		"message": "Привет! Версия 1.0"
	}
	
if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5000)