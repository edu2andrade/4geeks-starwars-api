from flask import jsonify
import domains.user.repository as Repository
import handle_response as Response

def create_new_user(data):
	if data['email'] is None or data['email'] == '':
		return Response.response_error('Email is not valid', 400)

	if data['name'] is None or data['name'] == '':
		return Response.response_error('Name is not valid', 400)

	return jsonify(Repository.create_new_user(data)), 201

def get_users_list():
	all_users = Repository.get_users_list()
	return Response.response_ok(all_users)

def get_single_user(user_id):
		user = Repository.get_single_user(user_id)
		if user is None:
			return Response.response_error('User not found', 404)

		return Response.response_ok(user.serialize())