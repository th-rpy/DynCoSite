import os
class Configuration(object):
	APPLICATION_DIR = os.path.dirname(os.path.realpath(__file__))
	DEBUG = True
	THREADED = True
	SQLALCHEMY_DATABASE_URI = 'sqlite:///%s/dynco.db' % APPLICATION_DIR
	SQLALCHEMY_TRACK_MODIFICATIONS = False
