import lib.qrcode
import lib.shorturl
import lib.s3

from flask import Flask, request
app = Flask(__name__)


@app.route("/health-check", methods=["GET"])
def healthcheck():
    return {
        'status': 'healthy'
    }, 200


@app.route("/qrcode", methods=["GET"])
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
                return {
                    'qrcode': s3_file_name,
                    'url': url,
                    'shorturl': validaUrlCurta()
                }, 200

        except:
            return {
                'error': 'error generating objects'
            }, 400

    else:

        return {
            'error:': 'bad request',
            'url': [{
                'required': True,
                'lenght': '> 3'
            }]
        }, 400


if __name__ == '__main__':
    app.run(debug=True, port=5000)
