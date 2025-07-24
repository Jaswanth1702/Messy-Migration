from flask import jsonify
from marshmallow import ValidationError
from sqlalchemy.exc import IntegrityError
from werkzeug.exceptions import NotFound

def register_error_handlers(app):
    @app.errorhandler(ValidationError)
    def handle_validation(err):
        return jsonify({'status':'error','message':'Invalid input','data':err.messages}), 400

    @app.errorhandler(IntegrityError)
    def handle_integrity(err):
        return jsonify({'status':'error','message':'Database integrity error'}), 409

    @app.errorhandler(NotFound)
    def handle_not_found(err):
        return jsonify({'status':'error','message':'Resource not found'}), 404

    @app.errorhandler(Exception)
    def handle_generic(err):
        app.logger.exception(err)
        return jsonify({'status':'error','message':'Internal server error'}), 500
