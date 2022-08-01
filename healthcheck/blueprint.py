from flask import Blueprint, Response
import json

healthcheck_routes = Blueprint("healthcheck", __name__, url_prefix="/health-check")

@healthcheck_routes.route("", methods=["GET"])
def healthcheck():
    retorno = {
        'status': 'healthy'
    }

    return Response(
        json.dumps(retorno),
        200,
        content_type="application/json"
    )