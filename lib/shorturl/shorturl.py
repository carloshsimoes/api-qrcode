import pyshorteners

def encurtarURL(url):
    encurtador = pyshorteners.Shortener()    
    urlCurta = encurtador.tinyurl.short(url) 
    return urlCurta
