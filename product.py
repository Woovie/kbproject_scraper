import scraper_object
import shopify

class Product(scraper_object.ScraperObject):# product = Product(config).create_product("Shopify")
    def __init__(self):
        pass

    def create_product(self, product_type: str) -> self.__class__:
        if (product_type == "Shopify"):
            product = shopify.ShopifyProduct()
        return product

    def build_name(self):
        pass

    def build_uri(self):
        pass

    def build_images(self):
        pass

    def build_pre(self):
        pass

    def build_post(self):
        pass

    def build(self):
        self.build_pre()
        self.build_name()
        self.build_uri()
        self.build_images()
        self.build_post()