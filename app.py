from flask import Flask, Response
import json

from qrcode.blueprint import qrcode_routes
from healthcheck.blueprint import healthcheck_routes

app = Flask(__name__)

app.register_blueprint(qrcode_routes)
app.register_blueprint(healthcheck_routes)


@app.route("/", methods=["GET"])
def index():
    retorno = {
        "app": "Sistema de geração de QRCode",
        "version": 1.0
    }

    return Response(
        json.dumps(retorno),
        200,
        content_type="application/json"
    )



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
