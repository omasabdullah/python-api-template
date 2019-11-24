from flask import Flask, request, abort, json
from werkzeug.exceptions import HTTPException

app = Flask(__name__)

class ServerError(HTTPException):
    code = 400
    description = 'you fucked up'

@app.route('/login', methods=['POST'])
def login():
    json = request.get_json(silent=True)

    if not json:
        raise ServerError('did it again my mans')

    return jsonify({'status': 'success'})

@app.errorhandler(HTTPException)
def error_handling(error):
    response = error.get_response()
    response.data = json.dumps({
        'code': error.code,
        'name': error.name,
        'type': type(error).__name__,
        'description': error.description
    })
    response.content_type = 'application/json'
    return response


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
