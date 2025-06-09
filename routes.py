from flask import request, jsonify

from app import app
from models import EchoInput
from utils import increment_request_count, parse_request_data
from pydantic import ValidationError
import logging


@app.route("/echo", methods=["POST"])
def echo():
    try:
        data = parse_request_data(request)
        validated = EchoInput(**data)
        count = increment_request_count()

        logging.info(f"Request #{count} | Data: {validated.model_dump()}")
        return jsonify({
            "request_number": count,
            "echo": validated.model_dump()
        }), 200

    except ValidationError as e:
        logging.warning(f"Validation error: {e}")
        return jsonify(error="Validation failed", details=e.errors()), 400

    except ValueError as e:
        logging.warning(f"Value error: {e}")
        return jsonify(error=str(e)), 400

    except Exception as e:
        logging.exception("Unhandled error occurred")
        return jsonify(error=f"Internal server error {str(e)}"), 500
