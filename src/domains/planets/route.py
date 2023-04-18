from flask import request
from models.index import Planets
import domains.planets.controller as Controller

def planet_routes(app):
    @app.route('/planets', methods=['POST'])
    def create_new_planet():
        data = request.get_json()
        return Controller.create_new_planet(data)
    
    @app.route('/planets', methods=['GET'])
    def get_planet_list():
        return Controller.get_planet_list()

    @app.route('/planets/<int:planet_id>', methods=['GET'])
    def get_single_planet(planet_id):
        return Controller.get_single_planet(planet_id)