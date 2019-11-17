from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_options

bootstrap = Bootstrap()

def create_app(config_name):

    app = Flask(__name__)

    # Creating the app configurations
    app.config.from_object(config_options[config_name])

    # Initializing flask extensions
    bootstrap.init_app(app)

    # # registering the blue print
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # #setting config
    from.request import configure_request
    configure_request(app)

    return app





# from flask import Flask
# from .config import DevConfig #to make our application use the new configurations
# from flask_bootstrap import Bootstrap
# from config import config_options

# bootstrap=Bootstrap()

# def create_app(config_name):
#     app=Flask(__name__)

#     #creating the app configurations
#     app.config.from_object(config_options[config_name])

#     #initializing flask extensions
#     bootstrap.init_app(app)

#     #will add the views and forms

#     return app
# #initializing the application
# app = Flask(__name__,instance_relative_config = True)

# #setting up the configuration
# app.config.from_object(DevConfig) #to set up the configuration and pass in DevConfig subclass
# app.config.from_pyfile('config.py')

# #Initializing Flask extensions
# bootstrap = Bootstrap(app)

# from app import views
# from app import error

# def create_app(config_name):
#     #registering the blueprint
#     from.main import main as main_blueprint
#     app.register_blueprint(main_blueprint)

#     #setting config
#     from .request import configure_request
#     configure_request(app)

#     return app