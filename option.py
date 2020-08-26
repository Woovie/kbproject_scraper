import scraper_object, shopify
import uuid

class Option(scraper_object.ScraperObject):
    def __init__(self):
        pass

    def create_option(self, option_type: str) -> self.__class__:
        if (option_type == "Shopify"):
            option = shopify.ShopifyOption()
        return option

    def build_name(self):
        pass

    def build_price(self):
        pass

    def build_availability(self):
        pass

    def build_pre(self):
        pass

    def build_post(self):
        pass

    def build(self):
        self.build_pre()
        self.build_name()
        self.build_price()
        self.build_availability()
        self.build_post()
        return self