import configparser, logging, json, uuid

# My modules
import vendor, option, image, product

class ShopifyVendor(vendor.Vendor):
    def set_data(self, config: configparser.ConfigParser, url: str):
        self.config = config
        self.url = url
        self.scrape_url = f"{self.url}{self.config['shopify']['data_location']}"

class ShopifyProduct(product.Product):# Factory
    def build_name(self):
        self.name = self.json["title"]

    def build_uri(self):
        self.uri = f"{self.config['shopify']['product_prefix']}{self.json['handle']}"

    def build_images(self):
        self.images = []
        for image in self.json["images"]:
            self.images.append(self.build_image(image))

    def build_image(self, image: dict) -> image.Image:
        image_object = image.Image(image["src"])
        image_object.set_id(self.uuid, image_object.url)
        return image_object.build()

    def build_variants(self):
        self.variants = []
        for variant in self.json["variants"]:
            self.variants.append(self.build_variant(variant))

    def build_variant(self, variant: dict) -> option.Option:
        option_object = option.ShopifyOption()
        option_object.set_data(variant)
        option_object.set_featured_image(self.uuid)
        option_object.build()
        option_object.set_id(self.uuid, option_object.name)
        return option_object

    def set_data(self, config: configparser.ConfigParser, payload: dict):
        self.config = config
        self.json = payload

    def build_post(self):
        self.build_variants()

class ShopifyOption(option.Option):
    def set_data(self, payload: dict):
        self.json = payload

    def set_featured_image(self, namespace_uuid: uuid.UUID):
        if self.json['featured_image']:
            self.image = uuid.uuid5(namespace_uuid, self.json['featured_image']['src'])

    def build_name(self):
        self.name = self.json["title"]

    def build_price(self):
        self.price = self.json["price"]

    def build_availability(self):
        self.available = self.json["available"]