from advanced_python_training.app import db


class Game(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    genre = db.Column(db.String(120), index=True, unique=True)
    rating = db.Column(db.String(128))

    def __repr__(self):
        return '<Game {}>'.format(self.name)

    def save(self):  # pragma: no cover
        db.session.add(self)
        db.session.commit()

    def get_by_name(self, id_):
        return Game.query.filter_by(name=id_).first()

    def get_all(self):
        return Game.query.all()
