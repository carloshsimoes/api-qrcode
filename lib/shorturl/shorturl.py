import pyshorteners

def encurtarURL(url):
    s = pyshorteners.Shortener()    
    shortUrl = s.tinyurl.short(url) 
    return shortUrl
