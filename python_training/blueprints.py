from python_training.routes import health, training


def register_blueprints(app):
    app.register_blueprint(health.health)
    app.register_blueprint(training.training)
