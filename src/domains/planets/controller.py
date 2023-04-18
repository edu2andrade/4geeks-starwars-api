from flask import jsonify
import domains.planets.repository as Repository
import handle_response as Response

def create_new_planet(data):
    if data['name'] is None or data['name'] == '':
    	return Response.response_error('Name is required to create a new planet', 400)

    return jsonify(Repository.create_new_planet(data)), 201

def get_planet_list():
    all_planets = Repository.get_planet_list()
    return Response.response_ok(all_planets)

def get_single_planet(planet_id):
    planet = Repository.get_single_planet(planet_id)
    if planet is None:
        return Response.response_error('Planet not found!', 404)

    return Response.response_ok(planet.serialize())