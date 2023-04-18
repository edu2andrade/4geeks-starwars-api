from flask import jsonify
import domains.favorites.repository as Repository
import handle_response as Response

def create_new_fav_planet(user_id, planet_id):
    return Repository.create_new_fav_planet(user_id, planet_id)

def create_new_fav_character(user_id, character_id):
    return Repository.create_new_fav_character(user_id, character_id)

def delete_fav_planet(user_id, planet_id):
    return Repository.delete_fav_planet(user_id, planet_id)

def delete_fav_character(user_id, character_id):
    return Repository.delete_fav_character(user_id, character_id)