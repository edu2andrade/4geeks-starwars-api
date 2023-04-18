from models.db import db

class Planets(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    population = db.Column(db.Integer, nullable=False)

    favorites = db.relationship('Favorites', back_populates='planets')

    def __init__(self, name, population):
        self.name = name
        self.population = population
    
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name, 
            "population": self.population, 
        }