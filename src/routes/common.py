from flask import Blueprint, request, jsonify


def login():
    json = request.get_json(silent=True)

    # if not json:
    #     raise RequestError('No JSON found')

    return jsonify({'status': 'success'}), 200

def register():
    json = request.get_json(silent=True)

    email = json.get('email')
    password = json.get('password')

    return jsonify({
        'message': f'Success for {email}, {password}'
    }), 200
