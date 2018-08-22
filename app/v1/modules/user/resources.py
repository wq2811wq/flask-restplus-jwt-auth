# -*- coding: utf-8 -*-
# @Author: guomaoqiu
# @File Name: user.py
# @Date:   2018-08-18 17:00:27
# @Last Modified by:   guomaoqiu@sina.com
# @Last Modified time: 2018-08-21 23:05:38
import logging
# from app.v1.roles import role_required
# import role_required, api_doc_requerid
from flask import request, jsonify
from app import db
from app.v1.middleware_delete import  role_required
from app.v1.modules.auth.models import User
from app.v1.extensions.auth.jwt_auth import refresh_jwt, auth
from flask_restplus import Resource, Namespace, fields


user_ns = Namespace('user')

parser = user_ns.parser()
parser.add_argument('Authorization', type=str,
                    location='headers',
                    help='Bearer Access Token',
                    required=True)


@user_ns.route('/delete/<email>')
class DeleterUserRequired(Resource):
    # 删除用户，只有超级管理员才有权限，请求时携带角色为sa的access_token
    @user_ns.doc(parser=parser)
    @auth.login_required
    @role_required.permission(2)
    def delete(self, email):
        user = User.query.filter_by(email=email).first()
        # Get user if it is existed.
        if user is not None:
            # Delete action.
            db.session.delete(user)
            db.session.commit()

            print ("user {} deleted".format(user.username))
            return {"message": "user {} delete success.".format(user.username)}, 200
        else:
            return {"message": "user {} does not exist.".format(email)}, 404


