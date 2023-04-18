from flask import request
from models.index import Favorites
import domains.favorites.controller as Controller

def favorites_routes(app):
    @app.route('/favorite/planet/<int:planet_id>', methods=['POST'])
    def create_new_fav_planet(planet_id):
        user_id = request.get_json()['user_id']
        return Controller.create_new_fav_planet(user_id, planet_id)

    @app.route('/favorite/character/<int:character_id>', methods=['POST'])
    def create_new_fav_character(character_id):
        user_id = request.get_json()['user_id']
        return Controller.create_new_fav_character(user_id, character_id)

    @app.route('/favorite/planet/<int:planet_id>', methods=['DELETE'])
    def delete_fav_planet(planet_id):
        user_id = request.get_json()['user_id']
        return Controller.delete_fav_planet(user_id, planet_id)

    @app.route('/favorite/character/<int:character_id>', methods=['DELETE'])
    def delete_fav_character(character_id):
        user_id = request.get_json()['user_id']
        return Controller.delete_fav_character(user_id, character_id)
