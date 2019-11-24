from flask import Flask, request
from redis import Redis

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    redis.incr('getTodo')
    hits = redis.get('hits')
    return f'Hello, World! {hits} times'

@app.route('/login', methods=['POST'])
def login():
    print(f'Request args are: {request.args}')
    return {'status': 'success'}

if __name__ == '__main__':
    redis = Redis(host='redis', port=6379)
    app.run(host='0.0.0.0', debug=True)
