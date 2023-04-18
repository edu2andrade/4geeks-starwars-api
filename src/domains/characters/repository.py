from models.index import db, Characters

def create_new_character(data):
      new_character = Characters(data['name'], data['height'], data['mass'], data['gender'])
      db.session.add(new_character)
      db.session.commit()
      return new_character.serialize()

def get_character_list():
      all_characters = Characters.query.all()
      serialized_characters = list(map(lambda character: character.serialize(), all_characters))

      return serialized_characters

def get_single_character(character_id):
      character = Characters.query.get(character_id)
      return character