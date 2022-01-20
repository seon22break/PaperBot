from bs4 import BeautifulSoup

class Parser:

    soup : BeautifulSoup

    def setContentPage(self, contentPage):
        if not contentPage:
            return False
        try:
            self.soup = BeautifulSoup(contentPage, "html.parser")
            return True
        except:
            print("ERROR procesando la pagina")
            return False

    def getTitlePage(self) :
        return self.soup.title.get_text()

    def getBodyArticle(self,domain) :
        draw = ""
        finder = self.__getFinderClass(domain)

        for bodyCard in self.soup.find_all(class_=finder):
            for i in bodyCard.find_all("p"):
                if len(i.get_text().split(" ")) == 1:
                    continue

                draw += "\n"+str(i.get_text())
        
        
        return draw
    

    def __getFinderClass(self,domain):
        if domain == "www.elmundo.es":
            return "ue-c-article__body"
        elif domain == "elpais.com":
            return "a_c clearfix"
