"""
Python implementation of yahoo shopping API
More documentation about API you
can find at http://developer.yahoo.co.jp/webapi/shopping
"""

import sys
import json
import codecs
from functools import wraps
from furl import furl

if sys.version_info.major == 2:
    from urllib2 import urlopen
else:
    from urllib.request import urlopen


def get_and_decode_json_by_url(url):
    """
    Fetches JSON data be making GET query and decodes JSON
    """
    req = urlopen(url)
    reader = codecs.getreader("utf-8")
    return json.load(reader(req))


def query_yahoo_api(function):
    """
    Decorator that handles API queries to amazon. Its prepare environment
    for method call and handle response results for Yahoo service -
    dumps json and handle errors.
    """
    @wraps(function)
    def wrapper(self, **kwargs):
        # creating new instance of url request
        self.api_request = self._api_root.copy()
        # populating it with params and adding query path
        function(self, **kwargs)
        # adding appid to params
        self.api_request.args['appid'] = self.appid
        self.api_request.path.normalize()
        return get_and_decode_json_by_url(self.api_request.url)
    return wrapper


class YahooShoppingAPI(object):

    _api_root = furl(
        "http://shopping.yahooapis.jp/ShoppingWebService/V1/json")

    def __init__(self, appid):
        self.appid = appid

    @query_yahoo_api
    def product_search(self, **kwargs):
        """
        Search Product, for supporter parameters take a look at
        http://developer.yahoo.co.jp/webapi/shopping/shopping/v1/itemsearch.html
        """
        # adding url request prefix
        self.api_request.path.segments.append('itemSearch')
        # TODO: add some params validation???
        self.api_request.args.update(**kwargs)

    @query_yahoo_api
    def category_acquisition(self, category_id=1, **kwargs):
        """
        Category ID acquisition is an API that returns the category name,
        category structure of Yahoo! Shopping in real time.
        Developers will be able to obtain these information by
        specifying the category ID.
        http://developer.yahoo.co.jp/webapi/shopping/shopping/v1/categorysearch.html
        """
        self.api_request.path.segments.append('categorySearch')
        # TODO: add some params validation???
        kwargs['category_id'] = category_id   # XXX: use inspect instead of this
        self.api_request.args.update(**kwargs)
