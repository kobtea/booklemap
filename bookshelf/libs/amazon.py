import amazonproduct
from amazon_config import *  # noqa


class API:
    def __init__(self):
        self.api = amazonproduct.API(cfg=AMAZON_CONFIG)
        self.associate_tag = AMAZON_CONFIG['associate_tag']

    def to_dict(self, elem, index):
        d = {}
        d['index'] = index  # used to sort
        d['asin'] = elem.ASIN
        d['title'] = unicode(elem.ItemAttributes.Title)
        return d

    def find_by_keyword(self, keyword):
        # TODO: AWS.ECommerceService.NoExactMatches
        items = self.api.item_search('Books', Keywords=keyword)
        l = []
        for i, elem in enumerate(items):
            l.append(self.to_dict(elem, i))
        return l

    def find_by_asin(self, asin):
        api = amazonproduct.API(locale='jp')
        result = api.item_lookup(asin)
        for i, elem in enumerate(result.Items.Item):
            return self.to_dict(elem, i)

api = API()
