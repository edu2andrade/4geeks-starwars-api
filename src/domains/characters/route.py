from flask import request
from models.index import Characters
import domains.characters.controller as Controller

def character_routes(app):
    @app.route('/character', methods=['POST'])
    def create_new_character():
        data = request.get_json()
        return Controller.create_new_character(data)
    
    @app.route('/character', methods=['GET'])
    def get_character_list():
        return Controller.get_character_list()

    @app.route('/character/<int:character_id>', methods=['GET'])
    def get_single_character(character_id):
        return Controller.get_single_character(character_id)