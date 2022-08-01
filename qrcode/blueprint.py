from flask import Blueprint, Response, request
import json

import lib.qrcode
import lib.shorturl
import lib.s3

qrcode_routes = Blueprint("qrcode", __name__, url_prefix="/qrcode")

@qrcode_routes.route("", methods=["GET"])
def qrcode():

    url = request.args.get('url')
    exibirHtml = request.args.get('ishtml', 0)

    validaUrlCurta = lambda: lib.shorturl.encurtarURL(url) if len(url) > 40 else url

    if url is not None and len(url) > 3:

        try:
            lib.qrcode.gerarQRCode(validaUrlCurta(), r'qr.png')
            s3_file_name = lib.s3.enviarQRcode(r'qr.png')

            if exibirHtml == '1':
                return f"""
                <div align=center>
                    <img src='{s3_file_name}' />
                    <br />
                    <a href="{validaUrlCurta()}">{validaUrlCurta()}</a>
                </div>
                """, 200

            else:
                retorno =  {
                    'qrcode': s3_file_name,
                    'url': url,
                    'shorturl': validaUrlCurta()
                }
                return Response(
                    json.dumps(retorno),
                    200,
                    content_type="application/json"
                )

        except:

            retorno = {
                'error': 'error generating objects'
            }
            return Response(
                json.dumps(retorno),
                200,
                content_type="application/json"
            )


    else:

        retorno = {
            'error:': 'bad request',
            'url': [{
                'required': True,
                'lenght': '> 3'
            }]
        }
        return Response(
            json.dumps(retorno),
            400,
            content_type="application/json"
        )