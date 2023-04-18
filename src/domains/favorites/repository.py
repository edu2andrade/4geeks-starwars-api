from models.index import db, Favorites, Characters, Planets, User
from flask import jsonify

def create_new_fav_planet(user_id, planet_id):
    new_favorite_planet = Favorites(planet_id, None, user_id)
    db.session.add(new_favorite_planet)
    db.session.commit()
    return new_favorite_planet.serialize_planets()

def create_new_fav_character(user_id, character_id):
    new_favorite_character = Favorites(None, character_id, user_id)
    db.session.add(new_favorite_character)
    db.session.commit()
    return new_favorite_character.serialize_characters()

def delete_fav_planet(user_id, planet_id):
    user_favorites = User.query.get(user_id).serialize()['favorites']
    fav_to_delete = list(filter(lambda fav: fav['planet_id'] == planet_id, user_favorites))
    if fav_to_delete:
        user_favorites.remove(fav_to_delete[0])
        db.sesssion.remove(target, identifier, fn) # ???
        db.session.commit()
        print('favorites -->', user_favorites)
        return jsonify({ "message": "planet deleted from favorites"})
    else:
        return jsonify({ "message": "Planet not found in user's favorites."})

def delete_fav_character(user_id, character_id):
    pass