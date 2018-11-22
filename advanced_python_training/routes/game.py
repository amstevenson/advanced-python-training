from flask import Blueprint, Response, request
from advanced_python_training.models import Game
import logging
import json

game = Blueprint('game', __name__)

logger = logging.getLogger()


@game.route("/add-game", methods=["POST"])
def add_game():
    game_json = request.get_json()
    logger.debug('game json is {}'.format(game_json))
    try:
        if not game_json['name'] or not game_json['genre'] or not game_json['rating']:
            return Response(response=json.dumps({'message': 'one or more parameters not present'}),
                            mimetype='application/json',
                            status=500)

        game_name = game_json['name']
        game_rating = game_json['rating']
        game_genre = game_json['genre']

        logging.info('Game data name {}, genere {}, rating {}'.format(game_name,
                                                                      game_rating,
                                                                      game_genre))

        # Add game by calling models
        game = Game()
        game.name = game_name
        game.rating = game_rating
        game.genre = game_genre
        game.save()

        return Response(response=json.dumps({'message': 'Game has been added'}),
                        mimetype='application/json',
                        status=200)

    except Exception as ex:
        logger.error(ex)


@game.route("/all-games", methods=["GET"])
def all_games():
    try:
        model_games = Game().get_all()

        games = []
        [games.append({'name': model_game.name,
                       'rating': model_game.rating,
                       'genre': model_game.genre}) for model_game in model_games]

        return Response(response=json.dumps({'games': games}),
                        mimetype='application/json',
                        status=200)
    except Exception as ex:
        logger.error(ex)
