from models.db import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), nullable=False, default=True)

    favorites = db.relationship('Favorites', back_populates='user')

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "favorites": list(map(lambda favorites: favorites.serialize_favorites(), self.favorites))
        }

    def serialize_user(self):
        return {
            "id": self.id,
            "name": self.name,
        }