from urllib.parse import urlparse
import requests

class Url:

    allowed_methods = ["https","http"]
    allowed_domains = ["www.elmundo.es","elpais.com"]
    domain = ""
    def __parseUrl(self,url):

        if not url:
            print("ERROR: La url está vacia")
            return False
        
        try:
            components = urlparse(url)
        except Exception as e:
            print("ERROR:"+str(e))
            return False
        
        if components.scheme not in self.allowed_methods:
            print("ERROR: El metodo no esta permitido: "+ str(components.scheme) )
            return False

        if components.netloc not in self.allowed_domains:
            print("ERROR: El dominio no esta permitido: "+str(components.netloc))
            return False

        self.domain = components.netloc
        return True
    
    def getRequestPage(self,url):
        if not self.__parseUrl(url):
            return False

        return requests.get(url).text
        






