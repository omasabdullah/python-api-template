from flask import Flask, request, abort, jsonify
from werkzeug.exceptions import HTTPException

app = Flask(__name__)

class ServerError(HTTPException):
    code = 427
    description = 'you fucked up'

@app.route('/login', methods=['POST'])
def login():
    json = request.get_json(silent=True)

    if not json:
        raise ServerError('did it again my mans')

    return jsonify({'status': 'success'})

@app.errorhandler(HTTPException)
def error_handling(error):
    print(error.description)
    return jsonify({
        'message': error.description
    }), error.code


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
