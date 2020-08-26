import scraper_object

class Image(scraper_object.ScraperObject):# Factory
    def __init__(self, url: str):
        self.url = url

    def build_pre(self):
        pass

    def build_post(self):
        pass

    def build(self):
        self.build_pre()
        self.build_post()
        return self