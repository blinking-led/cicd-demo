from flask import Flask
from datetime import datetime

app = Flask(__name__)
request_count = 0

@app.route('/')
def hello():
    global request_count
    request_count += 1
    return {
        "service": "cicd-demo",
        "version": "2.0",
        "message": "Привет! Это сервис v2.0",
        "timestamp": datetime.now().isoformat(),
        "request_count": request_count
    }

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)