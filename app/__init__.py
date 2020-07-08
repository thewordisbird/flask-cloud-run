from flask import Flask
from config import DevelopmentConfig, ProductionConfig

from app.firebase_wrapper import Firebase

#Global Objects
firebase = Firebase()

def create_app(config=ProductionConfig):
    app = Flask(__name__)
    app.config.from_object(config)

    # Initialize Firbase Wrapper
    firebase.init_app(app)
    
    # Register Blueprint
    from app.routes import bp

    app.register_blueprint(bp)

    @app.route('/hello')
    def hello():
        return f"<p>Hello, World!</p>"
    
    return app

