from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY']='my_secret_key'
    # Register Blueprint
    from app.routes import bp

    app.register_blueprint(bp)

    @app.route('/hello')
    def hello():
        return f"<p>Hello, World!</p>"
    
    return app

