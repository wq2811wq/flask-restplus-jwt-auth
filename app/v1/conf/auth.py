# -*- coding: utf-8 -*-
# @Author: guomaoqiu
# @File Name: auth.py
# @Date:   2018-08-14 21:04:02
# @Last Modified by:   guomaoqiu@sina.com
# @Last Modified time: 2018-08-21 17:36:42

from flask_httpauth import HTTPTokenAuth
from itsdangerous import TimedJSONWebSignatureSerializer as JWT

# JWT creation.
jwt = JWT('UbuQgGIdry*H&&I@', expires_in=930)

# Refresh token creation.
refresh_jwt = JWT('Ag93ZQ3KcGg&KUhR', expires_in=17200)

# Email token creation
confirm_email_jwt = JWT('HuGIUMKXLoHi4Y2S', expires_in=3600)

# Auth object creation.
auth = HTTPTokenAuth('OAuth')

