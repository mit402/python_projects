import pyshorteners
url = input("ENTER THE URL: ")

def shortenurl(url):
    x = pyshorteners.Shortener()
    print(x.tinyurl.short(url))

shortenurl(url)