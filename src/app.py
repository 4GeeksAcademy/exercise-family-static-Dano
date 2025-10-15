"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from utils import APIException, generate_sitemap
from datastructures import FamilyStructure

app = Flask(__name__)
app.url_map.strict_slashes = False
CORS(app)

jackson_family = FamilyStructure('Jackson')

@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/members', methods=['GET'])
def get_members():
    return jsonify(jackson_family.get_all_members()), 200

@app.route('/members', methods=['POST'])
def add_member():
    body = request.get_json(silent=True)
    if body is None:
        return jsonify({'msg': 'Rellena el body.'}), 400

    required = ["first_name", "age", "lucky_numbers"] #mas atractivo que poner if not in en 3 ocasiones
    for field in required:
        if field not in body:
            return jsonify({'msg': f'El campo {field} es obligatorio.'}), 400

    new_member = {
        'id': body.get('id'),
        'first_name': body['first_name'],
        'age': body['age'],
        'lucky_numbers': body['lucky_numbers']
    }
    member_added = jackson_family.add_member(new_member)

    return jsonify({
        'first_name': member_added['first_name'],
        'id': member_added['id'],
        'age': member_added['age'],
        'lucky_numbers': member_added['lucky_numbers']
    }), 200

@app.route('/members/<int:id>', methods=['GET'])
def get_member(id):
    member = jackson_family.get_member(id)
    if member is None:
        return jsonify({'message': 'Miembro no existe'}), 404
    return jsonify({
        'first_name': member['first_name'],
        'id': member['id'],
        'age': member['age'],
        'lucky_numbers': member['lucky_numbers']
    }), 200

@app.route('/members/<int:id>', methods=['DELETE'])
def delete_member(id):
    deleted = jackson_family.delete_member(id)
    if not deleted:
        return jsonify({'message': 'Miembro no existe'}), 404
    return jsonify({
        'done': True,
        'msg': 'Miembro eliminado con exito'
        }), 200

if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=True)
