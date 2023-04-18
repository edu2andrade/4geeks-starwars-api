from models.index import db, Planets

def create_new_planet(data):
      new_planet = Planets(data['name'], data['population'])
      db.session.add(new_planet)
      db.session.commit()
      return new_planet.serialize()

def get_planet_list():
      all_planets = Planets.query.all()
      serialized_planets = list(map(lambda character: character.serialize(), all_planets))

      return serialized_planets

def get_single_planet(planet_id):
      planet = Planets.query.get(planet_id)
      return planet