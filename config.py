import os

class Config(object):
	SECRET_KEY = os.environ.get('SECRET_KEY') or 'galloping-elephants'
	SQLALCHEMY_DATABASE_URI = 'sqlite:////tmp/test.db'