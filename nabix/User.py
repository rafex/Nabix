'''
Created on 06/12/2017

@author: rafex
'''
from .__init__ import nabix
from .__init__ import data_base
from passlib.apps import custom_app_context as pwd_context
from itsdangerous import (TimedJSONWebSignatureSerializer
                          as Serializer, BadSignature, SignatureExpired)

class User(data_base.Model):
    __tablename__ = 'users'
    id = data_base.Column(data_base.Integer, primary_key=True, unique=True)
    username = data_base.Column(data_base.String(20), index=True, unique=True)
    password_hash = data_base.Column(data_base.String(150))

    def hash_password(self, password):
        self.password_hash = pwd_context.encrypt(password)

    def verify_password(self, password):
        return pwd_context.verify(password, self.password_hash)

    def generate_auth_token(self, expiration=600):
        s = Serializer(nabix.secret_key, expires_in=expiration)
        return s.dumps({'id': self.id})

    @staticmethod
    def verify_auth_token(token):
        s = Serializer(nabix.secret_key)
        try:
            data = s.loads(token)
        except SignatureExpired:
            return None    # valid token, but expired
        except BadSignature:
            return None    # invalid token
        user = User.query.get(data['id'])
        return user
