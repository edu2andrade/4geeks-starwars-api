from flask import jsonify
import domains.characters.repository as Repository
import handle_response as Response

def create_new_character(data):
    if data['name'] is None or data['name'] == '':
    	return Response.response_error('Name is required to create one character', 400)

    return jsonify(Repository.create_new_character(data)), 201

def get_character_list():
    all_characters = Repository.get_character_list()
    return Response.response_ok(all_characters)

def get_single_character(character_id):
    character = Repository.get_single_character(character_id)
    if character is None:
        return Response.response_error('Character not found!', 404)

    return Response.response_ok(character.serialize())