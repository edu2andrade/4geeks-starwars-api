from models.index import db, User

def create_new_user(data):
    new_user = User(data['name'], data['email'], data['password'])
    db.session.add(new_user)
    db.session.commit()
    return new_user.serialize()


def get_users_list():
    all_users = User.query.all()
    serialized_users = list(map(lambda user: user.serialize(), all_users))
    return serialized_users


def get_single_user(user_id):
    user = User.query.get(user_id)
    return user