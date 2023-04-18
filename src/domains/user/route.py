from flask import request
from models.index import User
import domains.user.controller as Controller

def user_routes(app):
  @app.route('/users', methods=['POST'])
  def create_new_user():
    data = request.get_json()
    return Controller.create_new_user(data)

  @app.route('/users', methods=['GET'])
  def get_users_list():
    return Controller.get_users_list()

  @app.route('/users/<int:user_id>', methods=['GET'])
  def get_single_user(user_id):
    return Controller.get_single_user(user_id)