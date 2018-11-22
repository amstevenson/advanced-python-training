from advanced_python_training.routes import health, training, game


def register_blueprints(app):
    app.register_blueprint(health.health)
    app.register_blueprint(training.training)
    app.register_blueprint(game.game)
