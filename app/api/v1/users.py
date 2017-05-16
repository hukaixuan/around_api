# coding:utf-8
from flask import request
from ...models import db, User
from ...decorators import json, collection, etag
from . import api


# 获取所有用户
@api.route('/users/', methods=['GET'])
@etag
@json
@collection(User)
def get_users():
    return User.query

# 根据id获取单个用户
@api.route('/users/<int:id>', methods=['GET'])
@etag
@json
def get_user(id):
    return User.query.get_or_404(id)


# @api.route('/users/<int:id>/registrations/', methods=['GET'])
# @etag
# @json
# @collection(Registration)
# def get_user_registrations(id):
#     user = User.query.get_or_404(id)
#     return user.registrations


@api.route('/users/', methods=['POST'])
@json
def new_user():
    user = User().import_data(request.get_json(force=True))
    db.session.add(user)
    db.session.commit()
    return {}, 201, {'Location': user.get_url()}


# @api.route('/users/<int:id>/registrations/', methods=['POST'])
# @json
# def new_user_registration(id):
#     user = User.query.get_or_404(id)
#     data = request.get_json(force=True)
#     data['user_url'] = user.get_url()
#     reg = Registration().import_data(data)
#     db.session.add(reg)
#     db.session.commit()
#     return {}, 201, {'Location': reg.get_url()}


@api.route('/users/<int:id>', methods=['PUT'])
@json
def edit_user(id):
    user = User.query.get_or_404(id)
    user.import_data(request.get_json(force=True))
    db.session.add(user)
    db.session.commit()
    return {}


@api.route('/users/<int:id>', methods=['DELETE'])
@json
def delete_user(id):
    user = User.query.get_or_404(id)
    db.session.delete(user)
    db.session.commit()
    return {}
