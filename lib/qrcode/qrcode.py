import pyqrcode

def gerarQRCode(string, obj):

    stringQRCode = string.strip().replace(' ', '').lower()
    url = pyqrcode.create(stringQRCode)

    try:
        url.png(obj, scale=8)
    except:
        return None