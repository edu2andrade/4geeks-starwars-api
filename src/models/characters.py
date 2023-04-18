from models.index import db

class Characters(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120))
    height = db.Column(db.Integer)
    mass = db.Column(db.Integer)
    gender = db.Column(db.String(12))

    favorites = db.relationship('Favorites', back_populates='characters')

    def __init__(self, name, height, mass, gender):
        self.name = name
        self.height = height
        self.mass = mass
        self.gender = gender
    
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name, 
            "height": self.height, 
            "mass": self.mass, 
            "gender": self.gender, 
        }