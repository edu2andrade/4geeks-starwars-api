from models.db import db

class Favorites(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    planet_id = db.Column(db.Integer, db.ForeignKey('planets.id'), nullable=True)
    planets = db.relationship('Planets', back_populates='favorites')

    character_id = db.Column(db.Integer, db.ForeignKey('characters.id'), nullable=True)
    characters = db.relationship('Characters', back_populates='favorites')
    
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship('User', back_populates='favorites')

    def __init__(self, planet_id, character_id, user_id):
        self.planet_id = planet_id
        self.character_id = character_id
        self.user_id = user_id

    def serialize(self):
        return {
            "id": self.id,
            "planet_id": self.planet_id,
            "character_id": self.character_id,
            "user_id": self.user_id,
            "user": self.user.serialize()
        }

    def serialize_favorites(self):
        return {
            "planet_id": self.planet_id,
            "character_id": self.character_id,
            "user_id": self.user_id,
        }

    def serialize_characters(self):
        return {
            "id": self.id,
            "characters": self.characters.serialize(),
            "user_id": self.user_id,
        }

    def serialize_planets(self):
        return {
            "id": self.id,
            "planets": self.planets.serialize(),
            "user_id": self.user_id,
        }