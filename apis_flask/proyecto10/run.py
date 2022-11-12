from app_module import app

#app.config.from_pyfile('config.py')
app.config.from_object('configuration.DevelopmentConfig')
app.run()