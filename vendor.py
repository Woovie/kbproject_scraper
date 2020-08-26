import re

import scraper_object

class Vendor(scraper_object.ScraperObject):
    def __init__(self):
        self.price_regex = re.compile(r"(\d{1,3}\,){0,3}\d{1,3}(\.\d{2})?")